# Import Libraries
import os # Gives Python access to Linux commands
import time # Proves time related commands
from gpiozero import Buzzer # The GPIO Zero buzzer functions

# Set pin 22 as a buzzer
buzzer = Buzzer(22)

# sets the speed of the morse code reading
unit = 0.05
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
    ' ': '/'
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
    print('%s' % morseSequence, end="")
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
while True:
    msg = input("Quel est le message ?")
    convertToMorse(msg)
    print('done')
