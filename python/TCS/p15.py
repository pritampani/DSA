#Check Prime Number

class Solution:
    def isprime(self,n):
        if n==1:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        for i in range(5,int(n**0.5)+1):
            if n%i==0:
                return False
        return True


a = Solution()

print(a.isprime(1))   # False
print(a.isprime(2))   # True
print(a.isprime(3))   # True
print(a.isprime(4))   # False
print(a.isprime(5))   # True
print(a.isprime(17))  # True
print(a.isprime(18))  # False
print(a.isprime(19))  # True
print(a.isprime(25))  # False
print(a.isprime(97))  # True