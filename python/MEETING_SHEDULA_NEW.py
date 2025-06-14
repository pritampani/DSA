import datetime

class Meeting:
    def __init__(self, subject, start_time, end_time):
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f'Meeting: {self.subject}, {self.start_time} - {self.end_time}'

class Scheduler:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, subject, start_time, end_time):
        new_meeting = Meeting(subject, start_time, end_time)
        for meeting in self.meetings:
            if (new_meeting.start_time >= meeting.start_time and new_meeting.start_time < meeting.end_time) or (new_meeting.end_time > meeting.start_time and new_meeting.end_time <= meeting.end_time):
                raise ValueError('Conflict with existing meeting')
        self.meetings.append(new_meeting)

    def get_meetings(self):
        return self.meetings

scheduler = Scheduler()
scheduler.add_meeting('Meeting 1', datetime.datetime(2023, 2, 5, 10, 0), datetime.datetime(2023, 2, 5, 11, 0))


for meeting in scheduler.get_meetings():
    print(meeting)

f=open("participants.name.py","w")
name=f.write("TRIPTI\n")
name=f.write("SUKHPREET\n")
name=f.write("SURAJ\n")
name=f.write("VARSHA\n")
name=f.write("JASHOBANTA\n")
print(name)
print(name)
print(name)
f.close()

import csv

# meetings data
#meetings =  [["Meeting 1", "2023-01-05", "12:00", "Project Meeting"]]

# write meetings to a CSV file
with open("meetings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["meeting", "2023-02-05", "9:00", "PROJECT MEETING"])

meeting_id= int(input("enter the meeting id"))
passcode=str(input("enter the passcode"))
#Meeting will take place on Zoom
print(meeting_id)
print(passcode)
print("All the team members are requested to kindly join meeting sharply at 10:00am")


scheduler = Scheduler()
scheduler.add_meeting('Meeting 2', datetime.datetime(2023, 2, 7, 9, 0), datetime.datetime(2023, 2, 7, 10, 0))


for meeting in scheduler.get_meetings():
    print(meeting)

f=open("participants.name.py","w")
name=f.write("PRITAM\n")
name=f.write("PRACHI\n")
name=f.write("SHIVAM\n")
name=f.write("VARSHA\n")
name=f.write("JASHOBANTA\n")
info=f.write("New meeting is scheduled on 07-02-2023 at 9:00 am,\n Kindly join the meeting sharp at 9:00am")
info=f.write("Meeting details are shared in your emails")
print(name)
print(name)
print(name)
f.close()

import csv


with open("meetings.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(["meeting", "2023-02-07", "9:00", "PROJECT MEETING"])

meeting_id = int(input("enter the meeting id"))
passcode=str(input("enter the passcode"))
#Meeting will take place on Zoom
print(meeting_id)
print(passcode)
print("All the team members are requested to kindly join meeting sharply at 9:00")

import os
file_name="meetings.csv"
if os.path.exists(file_name):
    os.remove (file_name)
    print(f"{file_name}file deleted successfully")
else:
    print(f"{file_name}file not found")