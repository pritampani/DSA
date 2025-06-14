# def travel(source,dest):
#     if source==dest:
#         print("Reached")
#         return
    
#     travel(source+1,dest)
    


# source=0
# dest=100
# travel(source,dest)





# def fibo(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     a=fibo(n-1)
#     b=fibo(n-2)
#     return a+b

# print(fibo(10))






def countdig(n):
    c=0
    if n==0:
        return c
    c+=1
    return c + countdig(n//10)

print(countdig(1432))
