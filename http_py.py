# -*-coding:<coding:utf-8>-*-
import RPi.GPIO as GPIO 
import requests 
import json

#def webcontents_receive():
#   #url = "http://121.148.239.200:80/app/raspGetData"
#    url = "http://121.148.239.200:80/app/raspGetData"
#    url = "http://192.168.0.20:8081"
#    dataJson = requests.get(url, params = {}).json()
#    print(dataJson)    
#
#    for dat in dataJson:
#        print(dat.get('store_id'), dat.get('store_name'), dat.get('table_num'), dat.get('start_time'), dat.get('end_time'), dat.get('accupation_time'))
#
#        if dat.get('table_num') == 'tb1num01':
#            if dat.get('end_time') is not None:
#                led1_on1 = False
#                GPIO.output(table1_led1, False)
#            else:
#                led1_on1 = True
#                GPIO.output(table1_led1, True)
#

# send data from rasp to server
#def webcontents_send(store_id, store_name, table_num, table_value):
def webcontents_send():
    url = "http://192.168.0.20:8081/skyobserver/iotstate"
#   dataJson = requests.get(url, params = {}).json()

# Send Data to Server
# ==========================================
    datas = {
                "devName":"led1", 
                "devState":""
            }
    response = requests.post(url,data=datas )
# ==========================================
    print("status :", response.status_code)
    print(datas)

   #for dat in dataJson:
    for dat in datas:
        print(dat.get('devName'), dat.get('devState')) 



def getDataToServer():
    url = "http://192.168.0.20:8081/skyobserver/pitodata"   # Local Server
    getData = requests.get(url, params = {}).json()
    print(getData)

    for dat in getData:
        print(dat.get('devName'), dat.get('devState'))

webcontents_send()
print(" webcontents end")
getDataToServer()
print("getdata end")
