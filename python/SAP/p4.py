#Check prime number


class Solution:
    def isprime(self, a):
        if a==2 or a==3:
            return True
        if a%2==0:
            return False
        if a%3==0:
            return False
        for i in range(3, int(a**0.5) + 1, 2):
            if a%i==0:
                return False
        return True

a=Solution()
print(a.isprime(11))
print(a.isprime(12))
print(a.isprime(5))
