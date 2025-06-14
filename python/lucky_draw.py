a=int(input("enter the lucky number you want search between 1 to 100"))
lucky_number=26
for i in range(1):
    if lucky_number<=26:
        print("you have only two chance left")
        print(" sorry! you are close to your lucky number")
    elif lucky_number>=26:
        print("one chance left")
        print("you are far away from your lucky number")
    elif lucky_number==26:
        print("you won !")
        
        
