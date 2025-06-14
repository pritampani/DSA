from distutils import errors
import errno
import profile
import subprocess
from unittest import result

mera_data = subprocess.check_output(['netsh','wlan','show', 'profiles'])

data =  meta_data.decode('utf-8',errors = 'backslashreplace')

data = data.split('\n')

profile = []

for i in data:
    if "All User profile" in i:
        i = i.split(':')
        i = i[1]
        i = i[1;-1]
        profiles.append(i)
        
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-----------------------------------------------------------------------------")

for i in profile:
    try:
        result = subprocess.check_output(['netsh','wlan', 'show', 'profile', i,'key = clear'])
        result =  result.decode('utf-8',errors='backslashreplace')
        
        results = [b.split(':')[1][1:-1] for b in result if "Key Content" in b]
        
        try:
            print("{:<30}| {:<}".format(i, results[0]))


        except:
            IndexError:
                print("{:<30}| {:<}".formate(i,""))
    except subprocess.CalledProcessErroraa:
        print("Encoding Error Occured")
        