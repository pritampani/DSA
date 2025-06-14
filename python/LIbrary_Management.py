import os
from datetime import * as  dt
import pickle

def Introduction():
    print("Hello sir Welcome To our Library:")
    print("You can be a member of our library and enjoy reading different books")
    print("You can issue one book in your name at a time and at a rate of Rs.25")
    print("*****ALERT*****")
    print("if you return the book after the due date you will be fined Rs.10 per day")



def Add_new_book():
    f= open("books.dat",'wb')
    res=[]
    while True:
        bname=input("Enter book name:")
        author=input("Enter Auther name:")
        price=int(input("Enter book price:"))
        copies=int(input("Enter total number of copies:"))
        data=[bname,auther,price,copies]
        res.append(data)
        pickle.dump(res,f)
    f.close()


def Add_new_member():
    f= open("members.dat",'wb')
    rec=[]
    for i in range(1):
        name = input("Enter the name of new member:")
        address = input("enter member address")
        city = input("Enter the name of city:")
        district==input("Enter your District:")
        data2=[name,address,city,district]
        rec.append(loc)
        pickle.dump(rec,f)
        print("Congraulation! You are a member of our library")
    f.close()



def issue_book(curdt,rtrndt):
    srch=input("Enter the book you want yo issue:")
    f = open("book.dat",'rb')
    rec=[]
    while True:
        try:
            r=pickle.load(f)
            for i in r:
                rec.append(i)
        except EOFError:
            break
    f.close()
    c=0
    f2=open("book,dat",'wb')
    f1=open("issuedbook.dat",'wb')
    for i in rec:
        if j[0]==srch:
            nme=input("Enter the name of person who wants to issue the book")
            data=[srch,nme,j]
            pickle.dump(data,f1)
        print(nme,'has issued the book',srch,'on',curdt,'and should return the book before',rtrndt)
        c+=1
        