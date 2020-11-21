# Import Libraries
import os # Gives Python access to Linux commands
import time # Proves time related commands
from gpiozero import Button, Buzzer # The GPIO Zero buzzer functions

# Set pin 25 as a button input
button = Button(25)

# Set pin 22 as a buzzer
buzzer = Buzzer(22)

# sets the speed of the morse code reading
unit = 0.1
readUnit = 0.15

# number of units per type of symbol
dotLen = 1
dashLen = 3
signalSpacingLen = 1
letterSpacingLen = 3
wordSpacingLen = 7

morseChars = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' '
}

# A single morse dot
def dot(): 
    buzzer.on()
    time.sleep(dotLen * unit)
    buzzer.off()

# A single morse dash
def dash():
    buzzer.on()
    time.sleep(dashLen * unit)
    buzzer.off()

# The space between signal
def signalSpace(): 
    time.sleep(signalSpacingLen * unit)

# The space between letters
def letterSpace(): 
    time.sleep(letterSpacingLen * unit)

# The space between words
def wordSpace():
    time.sleep(wordSpacingLen * unit)

def beep(morseSequence):
    print('beep(%s)' % morseSequence)
    for i in range(0, len(morseSequence)):
        sound = morseSequence[i]
        if sound == '.' :
            dot()
            signalSpace()
        elif sound == '-' :
            dash()
            signalSpace()
        elif sound == ' ' :
            letterSpace()
        elif sound == '/' :
            wordSpace()

def convertToMorse(msg):
    morseSeq = ''
    for i in range(0, len(msg)):
        char = str(msg[i]).lower()
        morseSeq += morseChars[char] + ' '
    playMorse(morseSeq)
        
def playMorse(morse):
    print('playMorse(%s)' % morse)
    for i in range(0, len(morse)):
        signal = str(morse[i])
        beep(signal)
        letterSpace()

# Clears the terminal window
os.system('clear')

print("Morse code")
        
# Prompt the user for input
wasPressed = False
pressTime = 0
seq = ''
while True:
    isPressed = button.is_pressed
    time.sleep(readUnit)
    
    if not isPressed:
        # button is released
        buzzer.off()
        
        if wasPressed:
            wasPressed = False
            if pressTime >= unit * dashLen :
                seq += '-'
            else :
                seq += '.'
            pressTime = 0
            print(seq)
            continue
        else:
            # OVER
            if pressTime >= 3:
                print('OVER %s' % seq)
                playMorse(seq)
                break;
            
            # button is kept unpressed, increment time and continue
            pressTime += readUnit
            print('unpressed %i' % pressTime)
            continue

    # button is pressed
    buzzer.on()
    if wasPressed:
        # button is kept pressed, increment time and continue
        pressTime += readUnit
    else:
        wasPressed = True
        if pressTime >= unit * wordSpacingLen:
            seq += ' / '
        elif pressTime >= unit * letterSpacingLen:
            seq += ' '
        #elif pressTime >= unit * signalSpacingLen:
        #    seq += ''
        pressTime = 0
        print('seq %s' % seq)
 
    print('pressed %i' % pressTime)
    continue
