# lecture 58
# class Person:
#     name= "harry"
#     occupation = 'S.D'
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
    
# a =Person()
# #self ka matlb wo object jis par ye methord call ho raha he
# a.name = "subhem"
# a.occupation = "accoutant"

# b = Person()
# b.name = "prachi"
# b.occupation = 'HR'
# print(b.name,b.occupation)
# print(a.name,a.occupation)





#lecture 59












#lecture 61

# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def showdetails(self):
#         print(f"the name of {self.id} is {self.name}")
# class Programer(Employee):
#     print("this is the an example of inheritance")
      
# e1 = Employee("Rohan",400)
# e1.showdetails()
# e2 = Programer("pritam",1)
# e2.showdetails()


#lecture 62

# class Employee:
#     def __init__(self):
#         #we use '__' int the beginng of the variable to make some thing private
#         self.__name = "harry"

# a = Employee()
# #we can not ascess the private things in the class directly
# # print(a.name) 
# #we can ascess the private attriburte in the indirectly.
# print(a._Employee__name)
# print(a.__dir__())



#lecture 63
