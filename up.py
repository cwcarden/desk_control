import RPi.GPIO as GPIO
import time

#set GPIO mode to Broadcom SOC channel
GPIO.setmode(GPIO.BCM)
gpioPins =[2, 3]

for pin in gpioPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def up():
    try:
        GPIO.output(gpioPins[0], GPIO.LOW)
        time.sleep(36) #<-- set this for up and down time preset
        GPIO.output(gpioPins[0], GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()

def down():
    try:
        GPIO.output(gpioPins[1], GPIO.LOW)
        time.sleep(34) #<-- set this for up and down time preset
        GPIO.output(gpioPins[1], GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()

up()
