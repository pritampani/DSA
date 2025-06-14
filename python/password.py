import string
import random
import time
#from numpy import number
start = time.time()
s1 = string.ascii_lowercase
#print(s1)
#s2 = string.ascii_uppercase
#print(s2)
s3 = string.digits
#print(s3)
#s4 = string.punctuation
#print(s4)

plen=8
s=[]
s.extend(list(s1))
#s.extend(list(s2))
s.extend(list(s3))
#s.extend(list(s4))

print(s)
number_pass=int(input("enter number of password you want:"))
for i in range(number_pass):
    for y in range(plen,16):
        random.shuffle(s)
        print(''.join(s[0:y]))

end=time.time()
print(end-start)
