import RPi.GPIO as GPIO
import time
import requests
import json


# init led from server data
def webcontents_receive():
    url = "http://192.168.0.20:8080/skyobserver/iotstate"
    dataJson = requests.get(url, params = {}).json()
#   dataJson = requests.get(url).json()
    print(dataJson)


    # json file parshing
#   for dat in dataJson:
#       print(dat.get('devName'), dat.get('devState')) 

#       global led1_on1, led1_on2, led1_on3, led2_on1, led2_on2

#       if dat.get('devName') == 'led1':
#           if dat.get('devState') is not None:
#               led1_on1 = False
#               GPIO.output(table1_led1, False)
#           else:
#               led1_on1 = True
#               GPIO.output(table1_led1, True)

#       elif dat.get('devName') == 'led2':
#           if dat.get('devState') is not None:
#               led1_on2 = False
#               GPIO.output(led1, False)
#           else:
#               led1_on2 = True
#               GPIO.output(led2, True)


# send data from rasp to server
def webcontents_send(store_id, store_name, table_num, table_value):
    url = "http://121.148.239.200:80/app/raspSetData"
    r = requests.get(url, params = {'store_id' : store_id, 'store_name' : store_name, 'table_num' : table_num, 'table_value' : table_value})
#   r.encoding = 'utf-8'


# init All port and led
def initSetup():    
    GPIO.setmode(GPIO.BOARD)
#   GPIO.setup(table1_btn1, GPIO.IN)
#   GPIO.setup(table1_btn2, GPIO.IN)
#   GPIO.setup(table1_btn3, GPIO.IN)
#   GPIO.setup(table2_btn1, GPIO.IN)
#   GPIO.setup(table2_btn2, GPIO.IN)
#   #GPIO.setup(table2_btn3, GPIO.IN)
#   GPIO.setup(table1_led1, GPIO.OUT)
#   GPIO.setup(table1_led2, GPIO.OUT)
#   GPIO.setup(table1_led3, GPIO.OUT)
#   GPIO.setup(table2_led1, GPIO.OUT)
#   GPIO.setup(table2_led2, GPIO.OUT)
#   #GPIO.setup(table2_led3, GPIO.OUT)    
    webcontents_receive()


initSetup()
webcontents_send()
try : 
    while True:
        time.sleep(0.2)


except KeyboardInterrupt:
    pass
GPIO.cleanup()
