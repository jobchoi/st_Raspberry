import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# GPIO ports for the 7seg pins

segments =  (22,23,6,24,5,27,18)

fp = [18,27,22,23,24,25,5,6] # BCM
zero = [22,27,23,5,6,24]
one = [23,6]
two = [22,23,18,5,24,]
three = [22,23,18,6,24]
four = [27,18,23,6]
five = [22,27,18,6,24]
six = [27,5,24,6,18]
seven = [27,22,23,6]
eight = [22,23,6,24,5,27,18]
nine = [27,22,23,6,18]
#   GPIO 4,17,18,27,22,23,24,25,5,6 - BCM





for segment in segments:

    GPIO.setup(segment, GPIO.OUT)

    GPIO.output(segment, 0)


# GPIO ports for the digit 0-1 pins

#dig1 = 17  
#dig2 = 13
digits = (13, 17)


for digit in digits:

    GPIO.setup(digit, GPIO.OUT)

    GPIO.output(digit, 1)


num = {' ':(0,0,0,0,0,0,0),

    '0':(1,1,1,1,1,1,0),

    '1':(0,1,1,0,0,0,0),

    '2':(1,1,0,1,1,0,1),

    '3':(1,1,1,1,0,0,1),

    '4':(0,1,1,0,0,1,1),

    '5':(1,0,1,1,0,1,1),

    '6':(1,0,1,1,1,1,1),

    '7':(1,1,1,0,0,0,0),

    '8':(1,1,1,1,1,1,1),

    '9':(1,1,1,1,0,1,1)}


try:

    while True:

        n = time.ctime()[11:13]+time.ctime()[14:16]

        s = str(n).rjust(2)

        for digit in range(2):

            for loop in range(0,7):

                GPIO.output(segments[loop], num[s[digit]][loop])

               #if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                    #GPIO.output(25, 1)
               #else:
                    #GPIO.output(25, 0)

           #GPIO.output(digits[digit], 0)

            time.sleep(0.001)

           #GPIO.output(digits[digit], 1)

finally:

    GPIO.cleanup()
