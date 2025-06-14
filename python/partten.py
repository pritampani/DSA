#increasing triangle whith while loop 
def partten1():
    i=0
    while i<9:
        j=0
        while j<i:
            print("*" , end=' ')
            j=j+1
        i=i+1
        print()

def partten2():
    n=8
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()



#squre partten using for loop 
def partten3():
    n=5
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


#Decreasing triangle  star partten
def partten4():
    n=5
    for i in range(n):
        for j in range(i,n):
            print("*", end = ' ')
        print()
#
#
#
# right sided triangle
def partten5():
    n=5
    for i in range(n):
        for j in range(i,n):
            print(" ", end= " ")
        for j in range(i+1):
            print("*", end=' ')
        print()
#
#
#
#
#Right sided Decreased star partten
#
def partten6():
    n=5
    for i in range(n):
        for j in range(i+1):
            print(" ", end= " ")
        for j in range(i,n):
            print("*", end=" ")
        print()
#
#
#
#
#Hill star partten
def partten7():
    n=6
    for i in range(n):
        for j in range(i,n):
            print(" ", end=' ')
        for j in range(i):
            print("*",end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()

#Reverse Hill partten
def partten8():
    n=5
    for i in range(n):
        for j in range(i+1):
            print(" ", end=' ')
        for j in range(i,n-1):
            print("*", end = ' ')
        for j in range(i,n):
            print("*",end=' ')
        print()


#Diamond  star partten
def partten9():
    n=5
    for i in range(n-1):
        for j in range(i,n):
            print(" ", end=' ')
        for j in range(i):
            print('*',end=' ')
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i+1):
            print(' ', end=' ')
        for j in range(i,n-1):
            print("*",end=" ")
        for j in range(i,n):
            print("*", end=' ')
        print()




#__main__
while True:
    print("1.increasing triangle whith while loop ")
    print("2.program to draw 90 degree triangle")
    print("3.squre partten using for loop ")
    print("4.Decreasing triangle  star partten")
    print("5.left sided 90 degree trangle star partten")
    print("6.Right sided Decreased star partten")
    print("7.Hill star partten")
    print("8.Reverse Hill partten")
    print("9.Diamond  star partten")
    print("10.Break")
    ch=int(input("Enter your choise between (1-10)"))
    if ch==1:
        partten1()
    elif ch==2:
        partten2()
    elif ch==3:
        partten3()
    elif ch==4:
        partten4()
    elif ch==5:
        partten5()
    elif ch==6:
        partten6()
    elif ch==7:
        partten7()
    elif ch==8:
        partten8()
    elif ch==9:
        partten9()
    else:
        break
    