import string 



from itertools import permutations
 
 
# Get all permutations of [1, 2, 3]
s1 = string.ascii_lowercase
#print(s1)
s2 = string.ascii_uppercase
#print(s2)
s3 = string.digits
#print(s3)
s4 = string.punctuation
#print(s4)

s=[]
s.extend(list(s1))
# s.extend(list(s2))
# s.extend(list(s3))
# s.extend(list(s4))

print(s)
perm = permutations(s)
#len  = int(input("Enter the length of password:"))
for i in list(perm):
    password = "".join(i)
    print(password)

