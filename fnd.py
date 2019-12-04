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



def displayNumber(n):

    print("input Num : ", n)

    if n > 10:
        tp = (n // 10)
        print("tp : ", tp)
    op = getnum % 10

    print("tp arrList : ",arrList[tp])
    print("0 : ",zero, "\n1 : ",one, "\n2 : ",two,
          "\n3 : " , three, "\n4 : " ,four,
          "\n5 : " , five,  "\n6 : " ,six, 
          "\n7 : " , seven, "\n8 : " ,eight, 
          "\n9 : ",nine)
    print("arr : ",arrList[0][0])

#    if arrList[tp]:
#        for i, val in enumerate(arrList[tp]):
#            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
#            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
#            GPIO.setup(arrList[fp], GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
#            time.sleep(0.0005)
#        print("end :")


#clear
for i, val in enumerate(fp):
    GPIO.setup(fp[i], GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2

displayNumber(12)

''' 
while 1:
    for i, val in enumerate(zero):
        GPIO.setup(dig2, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        GPIO.setup(dig1, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        time.sleep(0.0005)
        print("three")
    #clear
    for i, val in enumerate(fp):
        GPIO.setup(fp[i], GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
    for i, val in enumerate(two):
        GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        GPIO.setup(two[i], GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        time.sleep(0.0005)
    for i, val in enumerate(fp):
        GPIO.setup(fp[i], GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
        print("one")
'''
#   GPIO.setup(one[i], GPIO.OUT, initial=GPIO.LOW)  
    
#GPIO.cleanup()





#clear
#for i, val in enumerate(fp):
#    GPIO.setup(fp[i], GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2



##def fndDigInit():
##    for index , value in enumerate(fp):
##        print("setup : %d" %fp[index])
##        GPIO.setup(fp[index],GPIO.OUT) # Dig : 1
#
#
#def diplayNum_FND():
#    for i in range(0,10):
#        fndNum(i)
#
##fndDigInit()
##diplayNum_FND()
