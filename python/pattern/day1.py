class solution:
    def printsquare(self,n):
        for i in range(n):
            for j in range(n):
                print('*',end='')
            print()
    def hollowsquare(self,n):
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1:
                    print('*',end='')
                else:
                    if j==0 or j==n-1:
                        print("*",end='')
                    print(" ",end='')
            print()
    
    def rounbus_star(self,n):
        for i in range(n):
            print(i*' ',end='')
            for j in range(n):
            
                print("*",end='')
            print()



a=solution()
#print(a.printsquare(4))
#print(a.hollowsquare(4))
#print(a.rounbus_star(4))
