# CamJam EduKit 1 - Basics
# Worksheet 5 - Button

# Import Libraries
import os # Gives Python access to Linux commands
import time # Proves time related commands
from gpiozero import Button, LED # The GPIO Zero button functions

# Set pin 25 as a button input
button = Button(25)

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

print("-------------")
print("Button + GPIO")
print("-------------")

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
    time.sleep(delay)
    red.off()

# The commands indented after this ‘while’ will be repeated
# forever or until ‘Ctrl+c’ is pressed.
while True:
    # If the button is pressed, button.is_pressed will be 'true'
    if (button.is_pressed):
        print("Button appuyé")
        bounce(0.1)
    else:
        os.system('clear') # Clears the screen
        print("En attente, appuie sur le bouton")
        time.sleep(0.5) # Sleep for 0.5 seconds

    
