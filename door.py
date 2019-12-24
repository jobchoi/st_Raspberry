import RPi.GPIO as GPIO
import time

# setmode 일때 40 -> 40번째 핀에 연결.
doorpin1 = 40
motor1 = 37
doorpin2 = 38
motor2 = 35
lock = 4.75
unlock = 4.75 # 값 미정



def pinInit():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(doorpin1, GPIO.IN)
	GPIO.setup(doorpin2, GPIO.IN)
	GPIO.setup(motor1, GPIO.OUT)
	GPIO.setup(motor2, GPIO.OUT)

pinInit()

p1 = GPIO.PWM(motor1, 50)
p2 = GPIO.PWM(motor2, 50)

p1.start(0)
p2.start(0)

while True:
	doorstate1 = GPIO.input(doorpin1)
	doorstate2 = GPIO.input(doorpin2)

	if doorstate1 is 1:
	
#print("door 1 : lock")
		p1.ChangeDutyCycle(lock)

	if doorstate2 is 1:
#		print("door 2 : lock")
		p2.ChangeDutyCycle(lock)

	if doorstate1 is 0:  
#	print("door 1 : unlock")
		p1.ChangeDutyCycle(unlock)

	if doorstate2 is 0:  
#	print("door 2 : unlock")
		p2.ChangeDutyCycle(unlock)

	time.sleep(0.1)


p.stop()                
GPIO.cleanup() 
