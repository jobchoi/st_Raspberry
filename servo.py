#!/usr/bin/env python
import RPi.GPIO as GPIO  
import time

pin = 12

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin, GPIO.OUT) 
p = GPIO.PWM(pin, 50)   

p.start(0)            
cnt = 0

#try:
#    while True:
#        print("0")
#        p.ChangeDutyCycle(12.5)
#        time.sleep(1)
#
#        print("1")
#        p.ChangeDutyCycle(10.0)
#        time.sleep(1)
#
#        print("2")
#        p.ChangeDutyCycle(7.5)
#        time.sleep(1)
#
#        print("3")
#        p.ChangeDutyCycle(5.0)
#        time.sleep(1)
#
#        print("4")
#        p.ChangeDutyCycle(2.5)
#        time.sleep(1)
#except KeyboardInterrupt:
#    p.stop()                
#    GPIO.cleanup() 
while(1):
    val = float(raw_input("input(3 ~ 7.5 ~ 12)="))
    if val == -1: break;

    p.ChangeDutyCycle(val)


p.stop()                
GPIO.cleanup() 

