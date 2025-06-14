from cmath import exp
from distutils.command.install_scripts import install_scripts
from email.headerregistry import Address
from fnmatch import fnmatch
from json import load
import pickle
import os
from re import L

def add():
    f= open("address.dat",'wb')
    Fname = input("\t\tEnter first name:")
    Lname = input("\t\tEnter last name:")
    Add = input("\t\tEnter Current address:")
    city = input("\t\tEnter city:")
    State= input("\t\tEnter the State:")
    pin = int(input("\t\tEnter the pin of current address:"))
    Ph = int(input("\t\tEnter phone number:"))
    l=[Fname,Lname,Add,city,State,pin,Ph]
    pickle.dump(l,f)

    f.close()


def display(c):
    c=0
    try:
        f=open("address.dat",'rb')
        l=pickle.load(f)
        if len(l)!=0:
            print("\t\t\tAddress details of all the persons are as follows:")
            print("\t\t[First name,Last name,Address,City,State,Pin,Phone, no.]")
            f.seek(0)
            while True:
                l= pickle.load(f)
                print("\t\t",l)
                c=1
    except:
        if c==0:
            print("\t\tThe file is empty")
        else:
            f.close()
        print()


def search(fn,ln):
    f= open("Address.dat",'rb')
    c=0
    try:
        while True:
            l=pickle.load(f)
            if l[0]==fn and l[1]==ln:
                print("\t\tAddress details of require customer is showen below:")
                print("\t\t\t[First name,Last name,Address ,city,State,Pin,Phone No.]")
                c=1
                break
    except:
        f.close()
    if c==0:
        print()
        print("No address for such person is exit")


def del_p():
    while True:
        fn = input("\t\tEnter name of person whose data to be deleted:")
        ln = input("\t\tEnter last of the person:")
        f=open("Address.dat",'rb')
        f1 = open("Temp.dat", 'wb')
        lt=[]
        c=0
        f.seek(0)
        try:
            while True:
                l=pickle.load()
                if l[0]==fn and l[1]==ln:
                    c=1
                else:
                    pickle.dump(l,f1)
        except:
            f.close()
            f1.close()
        if c==0:
            print()
            print("Record not found")
        else:
            print()
            print("\t\tDeleted Successfully")
        os.remove(Address.dat)
        os.rename("Temp.dat","Address.dat")
        print()



def del_al():
    f=open("Address.dat",'rb')
    f1 = open("Temp.dat",'wb')
    f.close()
    f1.close()
    os.remove("Address.dat")
    os.rename("Temp.dat","Address.dat")
    print()



def modify():
    f=open("Address.dat",'rb+')
    c=0
    print()
    while True:
        fnmatch = input("\t\tEnter first name of the person whose data want to be modified:")
        ln= input("\t\tEnter last name:")
        try:
            while True:
                t=f.tell()
                l=pickle.load(f)
                if l[0] ==fn and l[1] == fn:
                    a=input("Enter new address:")
                    c=input("Enter new city:")
                    s=input("Enter new state:")
                    p=input("Enter new pin for the place:")
                    ph=int(input("Enter new phone number:"))
                    lt = [fn,ln,a,c,s,p,ph]
                    f.seek(t)
                    pickle.dump(lt,f)
        except:
            print()
            print("Modified Successfully")
    f.close()


#__main__

print("\t\t\t\t\t\t\t*********************************")
print("\t\t\t\t\t\t\tWELCOME TO")
print("\t\t\t\t\t\t\tADDRESS BOOK MANAGEMENT")
print("\t\t\t\t\t\t\t***********************")
print()
while True:
    try:
        while True:
            print("Following are the works serial given. Choose the serial no of work that you want to do-->")
            print("\t\t1.Addition of new address")
            print("\t\t2.Display address details of all persons")
            print("\t\t3.Search and details of a particular person")
            print("\t\t4.Delete Adress data of particular person")
            print("\t\t5.Modify address of a person")
            print("\t\t6.Delete all data from address book:")
            print("\t\t7.Exit")
            print()
            print()
            print()
            ch = int(input("Enter serial no.:"))
            print()
            print()
            if ch==1:
                print()
                n=1
                add()
            elif ch==2:
                print()
                n=1
                display()
            elif ch==3:
                print()
                fn=input("\t\tEnter First name:")
                ln=input("\t\tEnter Last name:")
                n=1
                search(fn,ln)
            elif ch==4:
                print()
                n=1
                del_p()

            elif ch==5:
                print()
                n=1
                modify()
            elif ch==6:
                print()
                n=1
                del_al()
            elif ch==7:
                print()
                print("Thank You! Hoping meet again")
                break
            else:
                n=3
                break
    except:
        continue
    if n==3:
        print("\t\t\tPlease enter a valid serial number")
        print()
    elif n==2:
        break
    