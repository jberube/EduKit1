# CamJam EduKit 1 - Basics
# Worksheet 4 - User Input
# Import Libraries
import os # Allows you to interact with the operating system
import time # A collection of time related commands
from gpiozero import LED # The LED functions from GPIO Zero

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)
os.system('clear') # Clears the terminal window

while True:
    # Ask the user which colour LED to blink
    print("Quelle LED veux-tu faire clignoter?")
    print("1: Rouge?")
    print("2: Jaune?")
    print("3: Vert?")
    print("q: Quitter")
    led_choice = input("Fais ton choix: ")
    
    # Quit before converting to a number
    if led_choice == 'q':
        break;

    # Ensure that the led_choice variable is a whole number (integer)
    led_choice = int(led_choice)

    # Ask the user how many times they want the LED to blink
    count = input("Combien de clignotement?")

    # Ensure that the count variable is a whole number (integer)
    count = int(count)

    # Sets the variable 'LEDChoice' to be the LED choice
    if led_choice == 1:
        print("Tu as choisi la LED rouge")
        LEDChoice = red
    elif led_choice == 2:
        print("Tu as choisi la LED jaune")
        LEDChoice = yellow
    elif led_choice == 3:
        print("Tu as choisi la LED verte")
        LEDChoice = green
     
     # If we have chosen a valid choice, flash the LED
    if led_choice > 0:
        # While the count variable is greater than zero
        while count > 0:
            LEDChoice.on() # Turn the chosen LED on
            time.sleep(0.04) # Sleep for 1 second
            LEDChoice.off() # Turn the chosen LED off
            time.sleep(0.08) # Sleep for 2 seconds
            count = count - 1 # Decrease the count by one
