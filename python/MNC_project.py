def employee_detailes(EMPLOYEE):
    e_name=input("enter your name"):
    e_ID=int(input("enter your ID"))
i   e_addr=input("enter your address")
    e_salary=float(input("enter employee salary"))
    e_role=input("enter employee role in company")
    data=[e_name,e_ID,e_addr,e_salary,e_role]
    EMPLOYEE.append(data)
    
def employee_resume(EMPLOYEE):
    print(" Kindly Enter your resume")
    emp_name=input("Enter your name")
    emp_age=int(input("Enter your age"))
    emp_skill=_int(input("Enter how many skill you have:"))
    skill=[]
    for i in range(emp_skill):
        skill=input("Enter the skill name:")
    emp_Working_exprience=int(input("Enter your working exprience"))
    emp_salary_needed=float(input("Enter expeted salary from us "))
    emp_emailid=int(input("Enter a valid emailid"))
    data=[emp_name,emp_age,emp_skill,skill,emp_Working_exprience,emp_salary_needed,emp_emailid]
    EMPLOYEE.append(data)

def employee_Previous_company_details(EMPLOYEE):
    print("ENTER YOUR PREVIOUS COMPANY DETAILS")
    company_name = input("Enter your  company name")
    company_ID = int(input("Enter company ID"))
    company_website_link = int(input("Enter company website hompage link"))
    company_Role = input("Enter your role:")
    company_salary = float(input("Enter you salary"))
    company_expriences = input("Enter the number of year/month you work for the company:")
    data = [company_name,company_ID,company_website_link,company_Role,company_salary,company_expriences]
    EMPLOYEE.append(data)


