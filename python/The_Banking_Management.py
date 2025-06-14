import pickle
import os
import pathlib

class Account:
    accNo=0
    name=''
    add=''
    dist=''
    deposit=0
    type=''


    def createAccount(self):
        self.accNo=int(input("Enter the account no:"))
        self.name =input("Enter the account holder name:")
        self.add= input("Enter the Address:")
        self.dist=input("Enter the District:")
        self.type=input("Enter your type of account[C/S]:")
        self.deposit = int(input("Enter the Intial amount(>=500 for Saving and >=1000 for current)"))
        print("\n\n\nAccount Created")


    def showAccount(self):
        print("Account Number:",self.accNo)
        print("Account holder name:",self.name)
        print("Type of Account:",self.type)
        print("Balance:",self.deposit)


    def modifyAccount(self):
        print("Account Number:",self.accNo)
        print("Account holder name:",self.name)
        print("Type of Account:",self.type)
        print("Balance:",self.deposit)


    def depositAmmount(self,amount):
        self.deposit+=amount

    def withdrawAmmount(self,amount):
        self.deposit-=amount

    def report(self):
        print(self.accNo,"",self.name,"",self.add,"",self.dist,"",self.deposit)

    def getAccountNo(self):
        return self.accNo
    def getAccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit


    def intro():
        print("\t\t\t\t\t************************")
        print("\t\t\t\tBANKING MANAGEMENT SYSTEM")
        print("\t\t\t\t\tWELCOME TO DS BANK")
        print("PLEASE PRESS ENTER TO CONTINUE")
        input()


    def writeAccount():
        account=Account()
        account.createAccount()
        writeAccountsFile(account)

    def displayAll():
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open("accounts.data",'rb')
            mylist = pickle.load(infile)
            for item in mylist:
                print(item.accNo,"",item.name,"",item.type,"",item.deposit)
            infile.close()
        else:
            print("No records to display")


    def displaySp(num):
        file = pathlib.Path("accounts.data")
        if file.exists():
            infile = open("accounts.data",'rb')
            mylist = pickle.load(infile)
            infile.close()
            found = False
            for item in mylist:
                if item.accNo == num:
                    print("Your account Balance is=",item.deposit)
                    found = True
        else:
            print("No record to Search")
        if not found:
            print("NO existing record with this number")

    def depositAndWithdraw(num1,num2):
        file = pathlib.Path("account.data")
        if file.exists():
            infile = open('account.data','rb')
            mylist = pickle.load(infile)
            infile.close()
            os.remove("account.data")
            for item in mylist:
                if item.accNo==num1:
                    if num2==1:
                        amount=int(input("Enter the amount of deposit:"))
                        item.deposit+=ammount
                        print("Your account is update")
                    elif num2==2:
                        amount=int(input("Enter the ammount to withdraw:"))
                        if ammount <=item.deposit:
                            item.deposit-=amount
                        else:
                            print("You can not withdraw large ammount")
                else:
                    print("No record to Search")
                    outfile=open("newaccounts.data",'wb')
                    pickle.dump(mylist,outfile)
                    outfile.close()
                    os.rename('newaccounts.data','account.data')

    def DeleteAccount(num):
        file = pathlib.Path('accounts.data')
        if file.exists():
            infile = open('accounts.data','rb')
            oldlist= pickle.load(infile)
            infile.close()
            newlist = []
            for item in oldlist:
                if item.accNo !=num:
                    newlist.append(item)
            os.remove(accounts.data)
            outfile = open('newaccounts.data','wb')
            pickle.dump(newlist,outfile)
            outfile.close()
            os.rename('newaccounts.data','accounts.data')


    def modifyAccount(num):
        file = pathlib.Path('accounts.data')
        if file.exists():
            infile = open('accounts.data','rb')
            oldlist =pickle.load(infile)
            infile.close()
            os.remove('accounts.data')
            for item in oldlist:
                if item.acc.No == num:
                    item.name = input("Enter the account holder name:")
                    item.type  = input("Enter the account type:")
                    item.deposit=int(input("Enter the ammount:"))
                outfile =open('newaccounts.data','wb')
                pickle.dump(oldlist,outfile)
                outfile.close()
                os.rename('newaccounts.data','accounts.data')


    def writeAccountsFile(account):
        file =pathlib.Path('accounts.data')
        if file.exists():
            infile = open("accounts.data",'rb')
            oldlist=pickle.load(infile)
            oldlist.append(account)
            infile.close()
            os.remove('accounts.data')
        else:
            oldlist=[account]
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')


    #__main__
    ch = ''
    num = 0
    intro()
    while ch!=8:
        #system("cls")
        print("\tMAIN MENU")
        print("\t1.NEW ACCOUNT")
        print("\t2.DEPOSIT AMOUNT")
        print("\t3.WITHDRAW AMMOUNT")
        print("\t4.BALANCE ENQUIRY")
        print("\t5.ALL ACCOUNT HOLDER LIST")
        print("\t6.CLOSE AN ACCOUNT")
        print("\t7.MODIFY AN ACCOUNT")
        print("\t8.EXIT")
        print("\tSelect your option from (1-8)")
        ch=input()
        #system("cls")
        
        if ch == '1':
            writeAccount()
        elif ch =='2':
            num=int(input("\tEnter the account No.:"))
            depositAndWithdraw(num,1)
        elif ch == '3':
            num = int(input("\tEnter The account No."))
            depositAndWithdraw(num,2)
        elif ch == '4':
            num=int(input("\tEnter the account No.:"))
            displaySp(num)
        elif ch == '5':
            displayAll()
        elif ch == '6':
            num=int(input("\tEnter the account No.:"))
            DeleteAccount(num)
        elif ch == '7':
            num=int(input("\tEnter the account No.:"))
            modifyAccount(num)
        elif ch == '8':
            print("\tThanks for visiting DS Bank")
            break
        else:
            print("Invlide choice")
            ch = input("Enter your choice:")
            