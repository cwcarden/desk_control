import RPi.GPIO as IO
import time

#set GPIO mode to Broadcom SOC channel
IO.setmode(IO.BCM)
gpioPins =[2, 3]

for pin in gpioPins:
    IO.setup(pin, IO.OUT)
    IO.output(pin, IO.HIGH)

def up():
    IO.output(gpioPins[0], IO.LOW)

def down():
    IO.output(gpioPins[1], IO.LOW)

def stop_up():
    IO.output(gpioPins[0], IO.HIGH)

def stop_down():
    IO.output(gpioPins[1], IO.HIGH)
