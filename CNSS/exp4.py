import math

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.find_e(self.phi)
        self.d = self.find_d(self.e, self.phi)
    
    def find_e(self, phi):
        e = 2
        while e < phi:
            if math.gcd(e, phi) == 1:
                return e
            else:
                e += 1
        raise ValueError("Couldn't find a suitable 'e' value")
    
    def find_d(self, e, phi):
        k = 2
        d = ((k * phi) + 1) / e
        return d
    
    def encrypt(self, msg):
        C = pow(msg, self.e)
        C = math.fmod(C, self.n)
        return C
    
    def decrypt(self, C):
        M = pow(C, self.d)
        M = math.fmod(M, self.n)
        return M
    
    def get_keys(self):
        return (self.e, self.n), (self.d, self.n)


# Usage
p = 3
q = 7
rsa = RSA(p, q)

# Display keys
public_key, private_key = rsa.get_keys()
print(f'Public key: {public_key}')
print(f'Private key: {private_key}')

# Original message
msg = 11
print(f'Original message: {msg}')

# Encryption
C = rsa.encrypt(msg)
print(f'Encrypted message: {C}')

# Decryption
M = rsa.decrypt(C)
print(f'Decrypted message: {M}')
