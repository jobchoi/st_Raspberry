import RPi.GPIO as GPIO
import time

# FND Pin Dig position pin
# FND Left Top Dig : 1
# FND Right Bottom Dig : 2

GPIO.setmode(GPIO.BCM)

dig1 = 17  # 17
dig2 = 13 # DIg : 13 

#GPIO.setup(dig1,GPIO.OUT, initial=GPIO.LOW) # Dig : 1
#GPIO.setup(dig2,GPIO.OUT, initial=GPIO.LOW) # Dig : 2


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

# Test 

getnum = 5
#numList = ['zero','one', 'two', 'three', 'four','five','six','seven','eight','nine']
arrList = [zero, one, two, three, four, five, six, seven, eight, nine]

#clear
def fndcls(dig):
    GPIO.setup(dig, GPIO.OUT, initial=GPIO.HIGH)  # Dig 1(ten dig) on
    for i, val in enumerate(fp):
        GPIO.setup(fp[i], GPIO.OUT, initial=GPIO.HIGH) # fnd led off

def displayFNDNumber(inputNum):

    od = 0
    td = 0

    print("input Num : ", inputNum)
    print("0 : ",zero, "\n1 : ",one, "\n2 : ",two,
          "\n3 : " , three, "\n4 : " ,four,
          "\n5 : " , five,  "\n6 : " ,six, 
          "\n7 : " , seven, "\n8 : " ,eight, 
          "\n9 : ",nine)

    
    if inputNum >= 10:
        td = (inputNum // 10)
        od = inputNum % 10

        tdFND(td)
        odFND(od)

    else :
        od = inputNum % 10
        tdFND(0)
        odFND(od)
    
def tdFND(aptd):
    print("td arr : ",arrList[aptd])

    for i, val in enumerate(arrList[aptd]):
        GPIO.setup(dig1, GPIO.OUT, initial=GPIO.HIGH)  # Dig 1(ten dig) on
        GPIO.setup(dig2, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2 GPIO.setup(dig1, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2 


        GPIO.setup(arrList[aptd], GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        time.sleep(0.001)
        fndcls(dig1)

def odFND(apod):
    print("od arr : ",arrList[apod])
        
    for i, val in enumerate(arrList[apod]):
        GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # Dig 1(ten dig) off
        GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # Dig 2(one dig) on
        

        GPIO.setup(arrList[apod], GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        time.sleep(0.001)
        fndcls(dig2)


cnt = 90
while True:
    for i in range(0,100):
        displayFNDNumber(cnt)
        if cnt is 0:
            cnt = 100
    cnt -= 1

