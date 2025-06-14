import csv
import random
import string

def sch_new_meeting(meeting):
    date_of_meeting = input("Enter the date of meeting")
    start_time = input("Enter the staarting time")
    end_time = input("Enter the ending  time")
    email = input("Enter email id ")
    s1 = string.ascii_lowercase
    plen=8
    s=[]
    s.extend(list(s1))
    for i in range(1):
        for y in range(plen,16):
            random.shuffle(s)
            meeting_ID = ''.join(s[0:y])


    fields = [date_of_meeting,start_time,end_time,email,meeting_ID]
    print(meeting_ID)
    meeting.append(fields)
    with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\meeting.csv",'w') as f:
        csv_w = csv.writer(f,delimiter=',')
        csv_w.writerow(fields)
        return csv_w

def re_sch_meeting(meeting):
    with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\meeting.csv",'r',encoding='utf-8') as f:
        c=csv.reader(f,delimiter=' ', quotechar='|')
        for row in c:
            print(row)
        old_meeting_id = input("Enter the old meeting id:")
        if old_meeting_id==row[4]:
            meeting[0]= input("Enter the new date you want to schedul:")
            meeting[1] = input("Enter new meeting start time:")
            meeting[2] = input("Enter new end time:")
            meeting[3] = input("Enter new participante mail_id:")
        else:
            print("meeting_id is not matching")
        fields = [meeting[0],meeting[1],meeting[2],meeting[3]]
        meeting.append(fields)
        with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\meeting.csv",'w',newline=' ') as f:
            csv_w = csv.writer(f,delimiter=',')
            csv_w.writerow(fields)

def cancle_meeting(meeting):
     with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\meeting.csv",'w') as f:
        csv_w = csv.remover(f,delimiter=',')
        return csv_w

#__main__

while True:
    meeting = []
    print("1.Schedule new meeting")
    print("2.reshedule a meeting")
    print("3.cancle a meeting:")
    print("4.Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        sch_new_meeting(meeting)
    elif ch == 2:
        re_sch_meeting(meeting)
    elif ch == 3:
        cancle_meeting
    else:
        break
