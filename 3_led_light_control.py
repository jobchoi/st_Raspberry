import RPi.GPIO as GPIO

led_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(0)

while True:
    duty_s = input("Enter Brightness(0 to 100):")
    duty = int(duty_s)
      
    if(duty == 1000):
        pwm_led.stop()
        GPIO.cleanup()
        break
    else:
        pwm_led.ChangeDutyCycle(duty)
