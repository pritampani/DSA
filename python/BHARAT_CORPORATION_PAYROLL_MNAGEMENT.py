import pickle
import os

def Add():
    with open("Employee.dat",'wb') as f:
        d=[]
        emplno=int(input("Enter the Employee number:"))
        emplna=input("Enter Employee Name:")
        emplad=input("Enter the Address of Employee:")
        emplde=input("Enter the Designation of the Employee:")
        empldob=input("Enter Date Of Birth of the Employee:")
        bp=float(input("Enter Basic pay of the Employee:"))
        da=1.15*bp
        hra=0.30*bp
        pf=0.06*bp
        od=float(input("Enter The other Deduction:"))
        wd= int(input("Enter the number of Working Day:"))
        finalsal=(bp+da+hra+pf+od)
        totalsal=(finalsal//30)*wd
        if totalsal<=250000/12:
            Income_Tax=0
        elif totalsal>250000/12 and totalsal<=500000/12:
            Income_Tax=(totalsal*0.05)
        elif totalsal>500000/12 and totalsal<750000/12:
            Income_Tax=((12500/12)+(totalsal*0.10))
        elif totalsal>750000/12 and totalsal<1000000/12:
            Income_Tax=((37500/12)+(totalsal*0.15))
        elif totalsal>1000000/12 and totalsal<=1250000/12:
            Income_Tax=((75000/12)+(totalsal*0.20))
        elif totalsal>1250000/12 and totalsal<=1500000/12:
            Income_Tax=((1250000/12)+ (totalsal*0.25))
        elif totalsal>1500000/12:
            Income_Tax=((187500/12)+ (totalsal*0.30))
        data=[emplno,emplna,emplad,emplde,empldob,bp,da,hra,pf,od,Income_Tax,wd]
        d.append(data)
        pickle.dump(d,f)

def Show():
    with open("Employee.dat",'rb') as f:
        rec=pickle.load(f)
        if rec==[]:
            print("Your file is empty")
        else:
            
            print("THE PAYROLL OF BHARAT CORPORATION")
            n=1
            for i in rec:
                gross=i[5]+i[6]+i[7]
                td=i[8]+i[9]+i[10]
                net_pay=gross-td
                print('Record',n)
                print('Employee number:',i[0])
                print("Employee name:",i[1])
                print("Address:",i[2])
                print("Designation:",i[3])
                print("Date Of Birth:",i[4])
                print("Basic Pay:",i[5])
                print("Dearness Allowance:",i[6])
                print("House Rent Allowance:",i[7])
                print("Gross Pay:",gross)
                print("Income Tax Deducation:",i[10])
                print("Provision Fund Deduction:",i[8])
                print("Other Deduction:",i[9])
                print("Total Deduction:",td)
                print("Net Pay",net_pay)
                n=n+1





def Modify():
    with open("Employee.dat",'rb') as f:
        rec=pickle.load(f)
        emplno=int(input("Enter the Employee number to be modified:"))
        print("The field to be modified")
        Y=int(input("Enter 1 for designation, 2 for address,3 for date of birth:"))
        for i in rec:
            if i[0]==emplno:
                if Y==1:
                    Desig=input("Enter new designation:")
                    i[3]=Desig
                    print("Modification successful!")
                elif Y==2:
                    Adss=input("Enter New Address")
                    i[2]=Adss
                elif Y==3:
                    dob=input("Enter New date of Birth:")
                    i[4]=dob
                    print("Modification successful!")
                else:
                    print("Invlide input")


def Delete():
    with open("Employee.dat",'rb+') as f:
        rec=pickle.load(f)
    empno=int(input("Entre employee number to be detected:"))
    try:
        for i in rec:
            if i[0]==empno:
                rec.remove(i)
                print("Record is deleted!")
    except:
        print("Employee number is not found")
    with open("Employee.dat",'wb') as f:
        rec=pickle.dump(rec,f)

def Search():
    with open("Employee.dat",'rb') as f:
        rec=pickle.load(f)
    empno=int(input("Enter Employee number whose details to be search:"))
    try:
        for i in rec:
            if i[0]==empno:
                gross=i[5]+i[6]+i[7]
                td=i[8]+i[9]+i[10]
                net_pay=gross-td
                print('Record',n)
                print('Employee number:',i[0])
                print("Employee name:",i[1])
                print("Address:",i[2])
                print("Designation:",i[3])
                print("Date Of Birth:",i[4])
                print("Basic Pay:",i[5])
                print("Dearness Allowance:",i[6])
                print("House Rent Allowance:",i[7])
                print("Gross Pay:",gross)
                print("Income Tax Deducation:",i[10])
                print("Provision Fund Deduction:",i[8])
                print("Other Deduction:",i[9])
                print("Total Deduction:",td)
                print("Net Pay",net_pay)
    except:
        print("EMPLOYEE NUMBER DOES NOT EXIST!")


def Show_Data():
    with open("Employee.dat",'rb') as f:
        rec=pickle.load(f)
        print("Which Field You Want To Display")
        print("1.Employee number")
        print("2.Employee name")
        print("3.Employee Address")
        print("4.Designation")
        print("5.Date of birth")
        print("6.Basic pay")
        print("7.Dearness Allowance")
        print("8.House Rent Allowance")
        print("9.Income Tax Deducation")
        print("10.Provision Fund Deducation")
        print("11.Other Deduction")
        print("12.Number of working day")
        ch = int (input("Enter the field you want to Display(1-12):"))
        if ch>=1 and ch<=12:
            for i in rec:
                print(i[ch-1])
        else:
            print("DESIRED FIELD IS NOT FOUND!")





#************MAIN PROGRAM*************#
print("WELCOME TO BHARAT CORPARATION PAYROLL MANAGMENT SYSTEM")
while True:
    print("1.Add")
    print("2.Show")
    print("3.Modify")
    print("4.Delete")
    print("5.Search")
    print("6.Show_Data")
    print("7.Exit")
    ch=int(input("enter your Choice:"))
    if ch==1:
        Add()
    elif ch==2:
        Show()
    elif ch==3:
        Modify()
    elif ch==4:
        Delete()
    elif ch==5:
        Search()
    elif ch==6:
        Show_Data()
    elif ch==7:
        break
    else:
        print("Invlide choice!")


