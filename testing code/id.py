from gpiozero import Button
import time
print('all modules imported')

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

id = ""

#b1.wait_for_press()
print('hi')

for x in range (0,6):
	while True:
		if b1.is_pressed == True:
			id = id + '1'
			print('b1 pressed')
			time.sleep(0.25)
			break
		if b2.is_pressed == True:
			id = id + '2'
			print('b2 pressed')
			time.sleep(0.25)
			break
		if b3.is_pressed == True:
			id = id + '3'
			print('b3 pressed')
			time.sleep(0.25)
			break
		if b7.is_pressed == True:
			id = id + '4'
			print('b4 pressed')
			time.sleep(0.25)
			break
		if b8.is_pressed == True:
			id = id +  '5'
			print('b5 pressed;')
			time.sleep(0.25)
			break
		if b9.is_pressed == True:
			id = id + '6'
			print('b6 pressed')
			time.sleep(0.25)
			break

print(id)
