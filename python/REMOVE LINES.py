# PART 1 WRITE INTO THE MAIN FILE OR INPUT
# '''
main = open('main.txt','w')
n = int(input('enter number of lines to enter into the main file : '))
for i in range(n):
	main_input = input('enter data : ')
	main.write(main_input+'\n')
main.close()
# '''
# PART 2 COPY THE LINES TO TEMPORARY FILE EXCEPT THOSE WHICH ARE TO BE REMOVED

main = open('main.txt','r')
temp = open('temp.txt','w')
main_lines = main.readlines()
for line in main_lines:
	if ('a' in line) or ('A' in line):
		pass
	else:
		temp.write(line)
main.close()
temp.close()

# PART 3 COPY DATA FROM THAT TEMPORARY FILE TO THE MAIN FILE !!

temp = open('temp.txt','r')
main = open('main.txt','w')
temp_lines = temp.readlines()
for line in temp_lines:
	main.write(line)
temp.close()
main.close()

# PART 4 REMOVE THE TEMPORARY FILE !

import os 
os.remove('temp.txt')