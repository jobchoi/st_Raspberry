import RPi.GPIO as GPIO
import time



# FND Pin Dig position pin
# FND Left Top Dig : 1
# FND Right Bottom Dig : 2


def fndNum(n):
    dig1 = 17  
    dig2 = 13

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dig1,GPIO.OUT, initial=GPIO.LOW) # Dig : 1
    GPIO.setup(dig2,GPIO.OUT, initial=GPIO.LOW) # Dig : 2
    #   GPIO 4,17,18,27,22,23,24,25,5,6 - BCM

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


    if dig1 > 0: 
        GPIO.setup(dig1, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
    if dig2 > 0:
        GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2

    
    digNum1 = n % 10
    digNum10 = n / 10

#    GPIO.setup(dig1, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
#    GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2

    for i, val in enumerate(fp):
        GPIO.setup(fp[i], GPIO.OUT, initial=GPIO.HIGH)  

    # Display FND number
    if digNum10 == 0:
        for i, val in enumerate(zero):
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(zero):
            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        print("0")
    elif n== 1:
        for i, val in enumerate(zero):
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(zero):
            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(one[i], GPIO.OUT, initial=GPIO.LOW)  
        print("1")
    elif n==2:
        for i, val in enumerate(zero):
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(zero):
            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(two[i], GPIO.OUT, initial=GPIO.LOW)  
        print("2")
    elif n==3:
        for i, val in enumerate(zero):
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(zero):
            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(three[i], GPIO.OUT, initial=GPIO.LOW)  
        print("3")
    elif n==4:
        for i, val in enumerate(zero):
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(zero):
            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(four[i], GPIO.OUT, initial=GPIO.LOW)  
        print("4")
    elif n==5:
        for i, val in enumerate(zero):
            GPIO.setup(zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(zero):
            GPIO.setup(dig1, GPIO.OUT, initial=GPIO.LOW)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(dig2, GPIO.OUT, initial=GPIO.HIGH)  # FND pin 10 ON index:5(BCM-12) - Dig : 2
            GPIO.setup(five[i], GPIO.OUT, initial=GPIO.LOW)  
        print("5")
    elif n==6:
        for i, val in enumerate(zero):
            GPIO.setup(dig1,zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(six):
            GPIO.setup(six[i], GPIO.OUT, initial=GPIO.LOW)  
        print("6")
    elif n==7:
        for i, val in enumerate(zero):
            GPIO.setup(dig1,zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(seven):
            GPIO.setup(seven[i], GPIO.OUT, initial=GPIO.LOW)  
        print("7")
    elif n==8:
        for i, val in enumerate(zero):
            GPIO.setup(dig1,zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(eight):
            GPIO.setup(eight[i], GPIO.OUT, initial=GPIO.LOW)  
        print("8")
    elif n==9:
        for i, val in enumerate(zero):
            GPIO.setup(dig1,zero[i], GPIO.OUT, initial=GPIO.LOW)  
        for i, val in enumerate(nine):
            GPIO.setup(nine[i], GPIO.OUT, initial=GPIO.LOW)  
        print("9")
    else :
        print("not display")

    time.sleep(1)


#def fndDigInit():
#    for index , value in enumerate(fp):
#        print("setup : %d" %fp[index])
#        GPIO.setup(fp[index],GPIO.OUT) # Dig : 1


def diplayNum_FND():
    for i in range(0,10):
        fndNum(i)

#fndDigInit()
#diplayNum_FND()

# Test 
nn = 50 %10
numList = ['zero','one', 'two', 'three', 'four','five','six','seven','eight','nine']
print("\% : ",nn ,numList[nn])

