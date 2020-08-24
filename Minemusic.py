##### LIbrerías ####
import os
import time
import random
import pygame.mixer # Load the required library
from datetime import datetime
#### Variables ####
volumen = 1.0
debug = False	#True / False
Tmin=3*60*60
Tmax=6*60*60
#### Subrutinas ####
def log(msg):
    if debug: print (msg)

def Cargar():	#Carga canción aleatoria
	now = datetime.now()
	current_time = now.strftime("%H")
	if int(current_time) > 6:
		Selector = random.randrange(1,12)
		if   Selector==1:
			pygame.mixer.music.load('Music/calm1.mp3')
			log("calm1")
		elif Selector==2:
			pygame.mixer.music.load('Music/calm2.mp3')
			log("calm2")
		elif Selector==3:
			pygame.mixer.music.load('Music/calm3.mp3')
			log("calm3")
		elif Selector==4:
			pygame.mixer.music.load('Music/hal1.mp3')
			log("hal1")
		elif Selector==5:
			pygame.mixer.music.load('Music/hal2.mp3')
			log("hal2")
		elif Selector==6:
			pygame.mixer.music.load('Music/hal3.mp3')
			log("hal3")
		elif Selector==7:
			pygame.mixer.music.load('Music/hal4.mp3')
			log("hal4")
		elif Selector==8:
			pygame.mixer.music.load('Music/nuance1.mp3')
			log("nuance1")
		elif Selector==9:
			pygame.mixer.music.load('Music/nuance2.mp3')
			log("nuance2")
		elif Selector==10:
			pygame.mixer.music.load('Music/piano1.mp3')
			log("piano1")
		elif Selector==11:
			pygame.mixer.music.load('Music/piano2.mp3')
			log("piano2")
		elif Selector==12:
			pygame.mixer.music.load('Music/piano3.mp3')
			log("piano3")



#### Inicio ####
pygame.mixer.init()
volumen=0.3
pygame.mixer.music.set_volume(volumen)	#Volumen 0-1
pygame.mixer.music.load('System/listo.mp3')#Pista para saber si inició
pygame.mixer.music.play()
time.sleep(0.5)
print('Listo...')
volumen=1
pygame.mixer.music.set_volume(volumen)

#### Bucle ####
while True:
	now = datetime.now()
	current_time = now.strftime("%H")
	if int(current_time) > 6:
		log('Si hay loop')
		time.sleep(random.randrange(Tmin,Tmax))
		pygame.mixer.music.stop()
		Cargar()
		pygame.mixer.music.play()
	else:
		time.sleep(Tmin)