import RPi.GPIO as GPIO
import time
import requests
import json

# init led from server data
def webcontents_receive():
    url = "http://121.148.239.200:80/app/raspGetData"
    dataJson = requests.get(url, params = {}).json()
    print(dataJson)    
    
    # json file parshing
    #data = json.loads(dataString)
    for dat in dataJson:
        print(dat.get('store_id'), dat.get('store_name'), dat.get('table_num'), dat.get('start_time'), dat.get('end_time'), dat.get('accupation_time'))
        
        global led1_on1, led1_on2, led1_on3, led2_on1, led2_on2
        
        if dat.get('table_num') == 'tb1num01':
            if dat.get('end_time') is not None:
                led1_on1 = False
                GPIO.output(table1_led1, False)
            else:
                led1_on1 = True
                GPIO.output(table1_led1, True)
        
        elif dat.get('table_num') == 'tb1num02':
            if dat.get('end_time') is not None:
                led1_on2 = False
                GPIO.output(table1_led2, False)
            else:
                led1_on2 = True
                GPIO.output(table1_led2, True)
            
        elif dat.get('table_num') == 'tb1num03':
            if dat.get('end_time') is not None:
                led1_on3 = False
                GPIO.output(table1_led3, False)
            else:
                led1_on3 = True
                GPIO.output(table1_led3, True)
            
        elif dat.get('table_num') == 'tb2num01':
            if dat.get('end_time') is not None:
                led2_on1 = False
                GPIO.output(table2_led1, False)
            else:
                led2_on1 = True
                GPIO.output(table2_led1, True)
            
        elif dat.get('table_num') == 'tb2num02':
            print('dat[table_num] is tb2num02')
            if dat.get('end_time') is not None:
                print('led2_on02 is not null')
                led2_on2 = False
                GPIO.output(table2_led2, False)
            else:
                print('led2_on02 is null')
                led2_on2 = True
                GPIO.output(table2_led2, True)            
   
# send data from rasp to server
def webcontents_send(store_id, store_name, table_num, table_value):
    url = "http://121.148.239.200:80/app/raspSetData"
    r = requests.get(url, params = {'store_id' : store_id, 'store_name' : store_name, 'table_num' : table_num, 'table_value' : table_value})

# init All port and led
def initSetup():    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(table1_btn1, GPIO.IN)
    GPIO.setup(table1_btn2, GPIO.IN)
    GPIO.setup(table1_btn3, GPIO.IN)
    GPIO.setup(table2_btn1, GPIO.IN)
    GPIO.setup(table2_btn2, GPIO.IN)
    #GPIO.setup(table2_btn3, GPIO.IN)
    GPIO.setup(table1_led1, GPIO.OUT)
    GPIO.setup(table1_led2, GPIO.OUT)
    GPIO.setup(table1_led3, GPIO.OUT)
    GPIO.setup(table2_led1, GPIO.OUT)
    GPIO.setup(table2_led2, GPIO.OUT)
    #GPIO.setup(table2_led3, GPIO.OUT)    
    webcontents_receive()
    
    
'''def store_table_change(store_id, store_name, table_num, table_btn, table_led, table_pressed, led_on):    
    print(store_id)
    print(store_name)
    print(table_num)
    print(table_btn)
    print(table_led)
    print(table_pressed)
    print(led_on)
    
    
    sendstate = False
    
    if table_btn is 1:   
        if table_pressed == 0:
            led_on = not led_on
            print(led_on)
            table_pressed = 1
            sendstate = True
                
    else:            
        table_pressed = 0
        
    if led_on is True and sendstate is True:
        GPIO.output(table_led, True)
        table_value = 'ON'                
        webcontents(store_id, store_name, table_num, table_value)
        sendstate = False        
                
    elif led_on is False and sendstate is True:
        GPIO.output(table_led, False)
        table_value = 'OFF'                
        webcontents(store_id, store_name, table_num, table_value)
        sendstate = False '''

# store 1
store1_id = 'AA0101'
store1_name = '한울커피숍'

table1_num1 = 'tb1num01'
table1_num2 = 'tb1num02'
table1_num3 = 'tb1num03'

table1_btn1 = 11
table1_btn2 = 13
table1_btn3 = 15

table1_led1 = 8
table1_led2 = 10
table1_led3 = 12

table1_pressed1 = 0
table1_pressed2 = 0
table1_pressed3 = 0

led1_on1 = False
led1_on2 = False
led1_on3 = False

# store 2
store2_id = 'BB0101'
store2_name = '한울당구장'

table2_num1 = 'tb2num01'
table2_num2 = 'tb2num02'
#table2_num3 = 'tb2num03'

table2_btn1 = 29
table2_btn2 = 31
#table2_btn3 = 33

table2_led1 = 36
table2_led2 = 38
#table2_led3 = 40

table2_pressed1 = 0;
table2_pressed2 = 0;
#table2_pressed3 = 0;

led2_on1 = False
led2_on2 = False
#led2_on3 = False

initSetup()

try:    
    while True:
        time.sleep(0.2)
        btn11 = GPIO.input(table1_btn1)
        btn12 = GPIO.input(table1_btn2)
        btn13 = GPIO.input(table1_btn3)
        btn21 = GPIO.input(table2_btn1)
        btn22 = GPIO.input(table2_btn2)
#        btn23 = GPIO.input(table2_btn3)

        sendstate = False
        
        # store1 table1
        if btn11 is 1:   
            if table1_pressed1 == 0:
                led1_on1 = not led1_on1
                print(led1_on1)
                table1_pressed1 = 1
                sendstate = True
                    
        else:            
            table1_pressed1 = 0
            
        if led1_on1 is True and sendstate is True:
            GPIO.output(table1_led1, True)
            table_value = 'ON'                
            webcontents_send(store1_id, store1_name, table1_num1, table_value)
            sendstate = False        
                    
        elif led1_on1 is False and sendstate is True:
            GPIO.output(table1_led1, False)
            table_value = 'OFF'                
            webcontents_send(store1_id, store1_name, table1_num1, table_value)
            sendstate = False
            
        
        # store1 table2
        if btn12 is 1:   
            if table1_pressed2 == 0:
                led1_on2 = not led1_on2
                print(led1_on2)
                table1_pressed2 = 1
                sendstate = True
                    
        else:            
            table1_pressed2 = 0
            
        if led1_on2 is True and sendstate is True:
            GPIO.output(table1_led2, True)
            table_value = 'ON'                
            webcontents_send(store1_id, store1_name, table1_num2, table_value)
            sendstate = False        
                    
        elif led1_on2 is False and sendstate is True:
            GPIO.output(table1_led2, False)
            table_value = 'OFF'                
            webcontents_send(store1_id, store1_name, table1_num2, table_value)
            sendstate = False
            
        
        # store1 table3
        if btn13 is 1:   
            if table1_pressed3 == 0:
                led1_on3 = not led1_on3
                print(led1_on3)
                table1_pressed3 = 1
                sendstate = True
                    
        else:            
            table1_pressed3 = 0
            
        if led1_on3 is True and sendstate is True:
            GPIO.output(table1_led3, True)
            table_value = 'ON'                
            webcontents_send(store1_id, store1_name, table1_num3, table_value)
            sendstate = False        
                    
        elif led1_on3 is False and sendstate is True:
            GPIO.output(table1_led3, False)
            table_value = 'OFF'                
            webcontents_send(store1_id, store1_name, table1_num3, table_value)
            sendstate = False
            
        
        # store2 table1
        if btn21 is 1:   
            if table2_pressed1 == 0:
                led2_on1 = not led2_on1
                print(led2_on1)
                table2_pressed1 = 1
                sendstate = True
                    
        else:            
            table2_pressed1 = 0
            
        if led2_on1 is True and sendstate is True:
            GPIO.output(table2_led1, True)
            table_value = 'ON'                
            webcontents_send(store2_id, store2_name, table2_num1, table_value)
            sendstate = False        
                    
        elif led2_on1 is False and sendstate is True:
            GPIO.output(table2_led1, False)
            table_value = 'OFF'                
            webcontents_send(store2_id, store2_name, table2_num1, table_value)
            sendstate = False
            
            
        # store2 table2
        if btn22 is 1:   
            if table2_pressed2 == 0:
                led2_on2 = not led2_on2
                print(led2_on2)
                table2_pressed2 = 1
                sendstate = True
                    
        else:            
            table2_pressed2 = 0
            
        if led2_on2 is True and sendstate is True:
            GPIO.output(table2_led2, True)
            table_value = 'ON'                
            webcontents_send(store2_id, store2_name, table2_num2, table_value)
            sendstate = False        
                    
        elif led2_on2 is False and sendstate is True:
            GPIO.output(table2_led2, False)
            table_value = 'OFF'                
            webcontents_send(store2_id, store2_name, table2_num2, table_value)
            sendstate = False
                
        
        '''store_table_change(store1_id, store1_name, table1_num1, btn11, table1_led1, table1_pressed1, led1_on1)
            
        store_table_change(store1_id, store1_name, table1_num2, btn12, table1_led2, table1_pressed2, led1_on2)
     
        store_table_change(store1_id, store1_name, table1_num3, btn13, table1_led3, table1_pressed3, led1_on3)
    
        store_table_change(store2_id, store2_name, table2_num1, btn21, table2_led1, table2_pressed1, led2_on1)
    
        store_table_change(store2_id, store2_name, table2_num2, btn22, table2_led2, table2_pressed2, led2_on2) '''
    
#        if btn23 is 1: 
#            store_table_change(store2_id, store2_name, table2_num3, btn23, table2_led3, table2_pressed3, led2_on3)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()

