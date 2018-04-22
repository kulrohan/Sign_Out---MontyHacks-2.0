import paramiko
from gpiozero import Button, LED
import time

print('all modules imported')

#get student_id
b1 = Button(25)
b2 = Button(8)
b3 = Button(7)
b4 = Button(4)
b5 = Button(17)
b6 = Button(22)
b7 = Button(27)
b8 = Button(5)
b9 = Button(6)
b0 = Button(19)
be = Button(26)
bc = Button(13)

print('enter student id')

def enter_id():
    global id
    id = ""
    for x in range(0,5):
        while True:
            if b1.is_pressed == True:
                id = id+'1'
                print('b1 is pressed')
                time.sleep(0.25)
                break
            if b2.is_pressed == True:
                id = id+'2'
                print('b2 is pressed')
                time.sleep(0.25)
                break
            if b3.is_pressed == True:
                id = id+'3'
                print('b3 is pressed')
                time.sleep(0.25)
                break
            if b4.is_pressed == True:
                id = id+'4'
                print('b4 is pressed')
                time.sleep(0.25)
                break
            if b5.is_pressed == True:
                id = id+'5'
                print('b5 is pressed')
                time.sleep(0.25)
                break
            if b6.is_pressed == True:
                id = id+'6'
                print('b6 is pressed')
                time.sleep(0.25)
                break
            if b7.is_pressed == True:
                id = id+'7'
                print('b7 is pressed')
                time.sleep(0.25)
                break
            if b8.is_pressed == True:
                id = id+'8'
                print('b8 is pressed')
                time.sleep(0.25)
                break
            if b9.is_pressed == True:
                id = id+'9'
                print('b9 is pressed')
                time.sleep(0.25)
                break
	    if b0.is_pressed == True:
		id = id+'0'
		print('b0 is pressed')
		time.sleep(0.25)
    be.wait_for_press()
    return id

print(enter_id())




print('preparing to send id')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

location = 'Restroom E223B'

try:
    ssh.connect('172.20.10.3', username='kulnahor', password='Rohan2303') #string
except paramiko.SSHException():
    print "connection failed"
    quit()

print('connected')

ssh.exec_command('python sign_outW.py %s %s' %(id, location))
ssh.close()


print('task completed')
