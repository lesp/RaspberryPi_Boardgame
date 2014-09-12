import RPi.GPIO as GPIO
from time import sleep
import pygame

pygame.init()
pygame.mixer.init()

#Variables
#Sounds
snake = "wrong.mp3"
ladder = "correct.mp3"


#Resistors
r13 = 14
r39 = 15
r67 = 18
r72 = 23
#Pythons
s38 = 24
s47 = 25
s68 = 8
s99 = 7

#LED

d1 = 12
d2 = 16
d3 = 20
d4 = 21
d5 = 5
d6 = 6

#Button
button = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(r13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(r39,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(r67,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(r72,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(s38,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(s47,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(s68,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(s99,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(button,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(d1,GPIO.OUT)
GPIO.setup(d2,GPIO.OUT)
GPIO.setup(d3,GPIO.OUT)
GPIO.setup(d4,GPIO.OUT)
GPIO.setup(d5,GPIO.OUT)
GPIO.setup(d6,GPIO.OUT)

#Function to play sounds
def play_sound(x):
	pygame.mixer.music.load(x)
	pygame.mixer.music.play(1)
	while pygame.mixer.get_busy() == True:
		continue

while True:
    if GPIO.input(r13) == True:
        print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(r39) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(r67) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(r72) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(ladder)
    elif GPIO.input(s38) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(s47) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(s68) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(s99) == True:
    	print("button pressed")
        sleep(0.5)
        play_sound(snake)
    elif GPIO.input(button) == True:
    	print("BUTTON")
    	sleep(1)