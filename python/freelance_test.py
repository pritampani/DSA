import numpy as np
import math

# Stub for propssi (replace with actual CoolProp calls if available)
def propssi(zname, xname, xval, yname, yval, fluid):
    """
    Placeholder for thermodynamic property lookup.
    In real code, use CoolProp: PropsSI(zname, xname, xval, yname, yval, fluid).
    """
    # Example: return dummy property values
    if zname == "P":
        return 1e5 + 100 * xval - 0.01 * yval
    elif zname == "T":
        return 300 + 0.1 * yval
    elif zname == "S":
        return 1.0 + 0.001 * xval
    elif zname == "Q":
        return 0.5
    else:
        return -9999.0

# Main parameters
fluid = "water"
fname_out = "table1.dat"
xname, yname, zname = "D", "U", "P"

xmin, xmax = 0.02, 100.0
ymin, ymax = 2000e3, 3500e3
out_of_range = -9e9
ni, nj = 150, 150

# Arrays
xnow = np.zeros(ni)
ynow = np.zeros(nj)

ROOUT = np.zeros((ni, nj))
UOUT  = np.zeros((ni, nj))
HOUT  = np.zeros((ni, nj))
POUT  = np.zeros((ni, nj))
TOUT  = np.zeros((ni, nj))
CPOUT = np.zeros((ni, nj))
PHOUT = np.zeros((ni, nj))
DRYF  = np.zeros((ni, nj))
GA_PV = np.zeros((ni, nj))
ENTPY = np.zeros((ni, nj))

# Split density into intervals
xpon = (1.0 / (ni - 1)) * math.log(xmax / xmin)
const = xmin / math.exp(xpon)
for i in range(ni):
    xnow[i] = const * math.exp(xpon * (i + 1))

# Y values equally spaced
for j in range(nj):
    ynow[j] = ymin + (ymax - ymin) * float(j) / float(nj - 1)

# Loop over all values
for i in range(ni):
    xnoww = xnow[i]
    RONOW = xnoww
    for j in range(nj):
        ynoww = ynow[j]

        # Pressure
        znow = propssi("P", xname, xnoww, yname, ynoww, fluid)
        if znow == 0: znow = 100000.0
        PNOW = znow
        UNOW = ynoww

        # Temperature
        znow = propssi("T", xname, xnoww, yname, ynoww, fluid)
        if znow == 0: znow = 1000.0
        TNOW = znow

        # Entropy
        znow = propssi("S", xname, xnoww, yname, ynoww, fluid)
        if znow == 0: znow = 10000.0
        ENTNOW = znow

        # Dryness fraction
        znow = propssi("Q", xname, xnoww, yname, ynoww, fluid)
        if znow == 0: znow = 1.0
        QNOW = min(znow, 1.0)

        # Perturb for +/- differences
        DIFU = 0.0005 * ynow[j]
        DIFRO = DIFU * xnow[i] * xnow[i] / PNOW

        # Plus values
        ROPLUS = xnow[i] + DIFRO
        UPLUS  = ynow[j] + DIFU
        PPLUS  = propssi("P", xname, ROPLUS, yname, UPLUS, fluid)
        TPLUS  = propssi("T", xname, ROPLUS, yname, UPLUS, fluid)

        # Minus values
        ROMINUS = xnow[i] - DIFRO
        UMINUS  = ynow[j] - DIFU
        PMINUS  = propssi("P", xname, ROMINUS, yname, UMINUS, fluid)
        TMINUS  = propssi("T", xname, ROMINUS, yname, UMINUS, fluid)

        # Thermo calcs
        HNOW   = UNOW   + PNOW / RONOW
        HPLUS  = UPLUS  + PPLUS / ROPLUS
        HMINUS = UMINUS + PMINUS / ROMINUS
        CPNOW  = (HPLUS - HMINUS) / (TPLUS - TMINUS)

        # Protect against invalid logs
        if (HPLUS > 0 and HMINUS > 0 and 
            PPLUS > 0 and PMINUS > 0 and 
            ROPLUS > 0 and ROMINUS > 0 and
            PPLUS != PMINUS and ROPLUS != ROMINUS):

            PHEXP = math.log(HPLUS / HMINUS) / math.log(PPLUS / PMINUS)
            GAPV  = math.log(PPLUS / PMINUS) / math.log(ROPLUS / ROMINUS)
        else:
            PHEXP = float("nan")
            GAPV  = float("nan")

        # Store results
        ROOUT[i, j] = RONOW
        UOUT[i, j]  = UNOW
        HOUT[i, j]  = HNOW
        POUT[i, j]  = PNOW
        TOUT[i, j]  = TNOW
        CPOUT[i, j] = CPNOW
        PHOUT[i, j] = PHEXP
        DRYF[i, j]  = QNOW
        GA_PV[i, j] = GAPV
        ENTPY[i, j] = ENTNOW

# Write results to file
with open("all_tables.dat", "w") as f:
    f.write(f"NI, NJ = {ni}, {nj}\n")
    f.write("X VALUES:\n")
    f.write(" ".join(f"{val:.8e}" for val in xnow) + "\n")
    f.write("Y VALUES:\n")
    f.write(" ".join(f"{val:.8e}" for val in ynow) + "\n")

    properties = [
        ("DENSITY", ROOUT),
        ("INTERNAL ENERGY", UOUT),
        ("PRESSURE", POUT),
        ("TEMPERATURE", TOUT),
        ("ENTROPY", ENTPY),
        ("GA_PV", GA_PV),
        ("DRYNESS FRACTION", DRYF),
    ]

    for pname, parr in properties:
        f.write("\nBLANK\n")
        f.write(f"NEW PROPERTY, {pname}\n")
        for i in range(ni):
            f.write(f"I = {i+1:5d} DENSITY = {xnow[i]:15.8e}\n")
            f.write(" ".join(f"{parr[i, j]:.8e}" for j in range(nj)) + "\n")


"""

The main change made to the code was adding safety checks before logarithm calculations to prevent math domain error. In the original script, invalid values (zero or negative) sometimes entered math.log(), causing the program to crash. The updated code now verifies that all numerator and denominator values are positive and non-equal before computing logarithms. If the conditions are not met, it safely assigns NaN instead of stopping execution. This ensures the program runs fully, generates the output file, and marks invalid points without errors.
"""