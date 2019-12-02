import RPi.GPIO as IO
import time

#set GPIO mode to Broadcom SOC channel
IO.setmode(IO.BCM)
gpioPins =[2, 3]

for pin in gpioPins:
    IO.setup(pin, IO.OUT)
    IO.output(pin, IO.HIGH)

def up():
    try:
        IO.output(IOPins[0], IO.LOW)
        time.sleep(36)
        IO.output(IOPins[0], IO.HIGH)
    except KeyboardInterrupt:
        IO.cleanup()

def down():
    try:
        IO.output(IOPins[1], IO.LOW)
        time.sleep(36)
        IO.output(IOPins[1], IO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()
