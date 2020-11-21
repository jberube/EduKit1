# Import Libraries
#import os # Gives Python access to Linux commands
import time # Proves time related commands
from gpiozero import Button, Buzzer, LED # The GPIO Zero buzzer functions

# Set pin 25 as a button input
button = Button(25)


# cars lights
# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
amber = LED(23)
green = LED(24)

# pedestrians lights
# Set pins 17 and 27 to be LEDs
ped_green = LED(17)
ped_red = LED(27)
# Set pin 22 as a buzzer
buzzer = Buzzer(22)

frame = 20/60

def shutdown():
    red.off()
    amber.off()
    green.off()
    buzzer.off()
    ped_green.off()
    ped_red.off();
    
def nextFrame():
    time.sleep(frame)

# Diagnostic Boot Sequence
def diagSequence():
    red.blink()
    nextFrame()
    
    amber.blink()
    nextFrame()
    
    green.blink()
    nextFrame()
    
    diagButtonPressed = False
    while not diagButtonPressed:
        diagButtonPressed = button.is_pressed
        time.sleep(1/60)

    buzzer.blink()
    nextFrame()

    ped_red.blink()
    nextFrame()
    
    ped_green.blink()
    nextFrame()
    
    diagButtonPressed = False
    while not diagButtonPressed:
        diagButtonPressed = button.is_pressed
        time.sleep(1/60)
        
    shutdown()


# run some diagnosis sequence at boot
diagSequence()

# Configurations
phase1MinTime = 5 # 20
phase2Time = 3
phase3Time = 1
phase4Time = 4 # 4 to 7
phase5Time = 2
phase6Time = 6
phase7Time = 1

# Cars have green light
def phase1():
    green.on()
    ped_red.on()
    buttonPressed = False
    minTimeRemaining = float(phase1MinTime)
    
    while (minTimeRemaining > 0) or not buttonPressed:
        # detect button if it has not been pressed yet
        if not buttonPressed:
            buttonPressed = button.is_pressed
        # Loop
        minTimeRemaining = minTimeRemaining - frame
        nextFrame()
    # Cycle if over
    shutdown()
 
# Cars should stop if they can 
def phase2():
    amber.on()
    ped_red.on()
    time.sleep(phase2Time)
    shutdown()

# Nobody moves
def phase3():
    red.on()
    ped_red.on()
    time.sleep(phase3Time)
    shutdown()

# Cars have red light, pedestrians have green light and beeping
def phase4():
    red.on() # cars
    ped_green.on() # predestrians
    buzzer.blink(5/60)
    time.sleep(phase4Time)
    shutdown()

# Cars have red light
# Pedestrians have green light but should not start crossing, no sound
def phase5():
    red.on() # cars
    ped_green.blink(5/60) # predestrians
    time.sleep(phase5Time)
    shutdown()

def phase6():
    amber.blink(5/60) # cars
    ped_green.blink(5/60) # predestrians
    time.sleep(phase6Time)
    shutdown()

def phase7():
    amber.blink(5/60) # cars
    ped_red.on() # predestrians
    time.sleep(phase7Time)
    shutdown()

# main loop
while True:
    phase1()
    phase2()
    phase3()
    phase4()
    phase5()
    phase6()
    phase7()

# Get sure everything is closed when shut down
shutdown()
