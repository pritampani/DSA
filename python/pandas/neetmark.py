import pandas as pd

# Load the Excel file
file_path = "/Users/pritampani/Desktop/DSA/python/pandas/5_6113830201475468942.xlsx"

# Initialize the count
count_above_650 = 0

# Load the Excel file
xls = pd.ExcelFile(file_path)

# Iterate through each sheet in the Excel file
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    # Check the columns with 'Marks' in their name
    mark_columns = [col for col in df.columns if 'Marks' in col]
    for col in mark_columns:
        count_above_650 += (df[col] > 689 ).sum()

print(f"Number of serials with marks above 650: {count_above_650}")