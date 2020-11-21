# CamJam EduKit 1 - Basics
# Worksheet 2 - LEDs

# Import Libraries
import time # A collection of time related commands
from gpiozero import LED # The LED functions from GPIO Zero

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

def attente(delay) :
    print("attente")
    red.on()
    time.sleep(delay)
    yellow.on()
    time.sleep(delay)
    green.on()
    time.sleep(delay)
    red.off()
    time.sleep(delay)
    yellow.off()
    time.sleep(delay)
    green.off()
    time.sleep(delay)

def bounce(delay) :
    print("bounce")
    red.on()
    time.sleep(delay)
    red.off()
    yellow.on()
    time.sleep(delay)
    yellow.off()
    green.on()
    time.sleep(delay * 2)
    green.off()
    yellow.on()
    time.sleep(delay)
    yellow.off()
    red.on()
    
for i in range(1, 10):
    # attente(0.05 + i * 0.025)
    # attente(0.05)
    bounce(0.1)

time.sleep(0.1)
red.off()
