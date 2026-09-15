import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
led = 26
foto = 6
GPIO.setup(led, GPIO.OUT) #цифровой выход сделали 
GPIO.setup(foto, GPIO.IN)
state = 0
while True:
    state = GPIO.input(foto)
    if GPIO.input(foto):
        GPIO.output(led, GPIO.LOW)
    else:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.1)