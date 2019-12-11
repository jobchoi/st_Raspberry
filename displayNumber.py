from fnd import displayFNDNumber
import time

cnt = 50

while True:
    for i in range(0,50):
        displayFNDNumber(cnt)
        if cnt <= 0:
            cnt = 90
    cnt -= 1
