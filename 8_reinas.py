import pygame,sys
from pygame.locals import *


# Declaracion de constantes y variables
WHITE = (255,255,255)
TAMCASILLA = 60
FPSCLOCK = pygame.time.Clock()
tablero = pygame.image.load('tablerito.png')
reina = pygame.image.load('image.png')
win = pygame.image.load('win.jpg')


pygame.init()
TAMPANTALLA = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('Agente de las 8 reinas - jbamacg@miumg.edu.gt')


hayReina = [[False for x in range(8)] for y in range(8)] #Contiene falso si en la casilla [x][y] no hay una reina.

reinasPuestas = 0

#Funciones
def finDeJuego():
	if reinasPuestas == 8:
		return True
	else:
		return False


def clickEnCasilla(mousex,mousey):
	if mousex > 10 and mousex < 490 and mousey > 10 and mousey < 490:
		return True
	return False


def dibujarReinas():
	for x in range(8):
		for y in range(8):
			if hayReina[x][y]:
				TAMPANTALLA.blit(reina,(x*60 +10, y*60+10))

def invertirCasilla(x,y): 
	
	global reinasPuestas

	if hayReina[x][y]:
		hayReina[x][y] = False
		reinasPuestas = reinasPuestas-1
	else:
		hayReina[x][y] = True
		reinasPuestas = reinasPuestas+1


def movimientoLegal(x,y):
	if hayReina[x][y]: 
		return True
	else:
		#fila
		for col in range(8):
			if hayReina[col][y]:
				return False

		#columna
		for fila in range(8):
			if hayReina[x][fila]:
				return False
		
		#diagonales
		col = x
		fil = y
		while col < 8 and fil < 8:
			if hayReina[col][fil]:
				return False
			
			col = col+1
			fil = fil+1

		col = x
		fil = y
		while col >= 0 and fil >= 0:
			if hayReina[col][fil]:
				return False

			col = col-1
			fil = fil-1

		col = x
		fil = y

		while col >= 0 and fil < 8:
			if hayReina[col][fil]:
				return False

			col = col-1
			fil = fil+1

		col = x
		fil = y

		while col < 8 and fil >= 0:
			if hayReina[col][fil]:
				return False

			col = col+1
			fil = fil-1
		return True

#Loop 
while True:

	TAMPANTALLA.blit(tablero,(0,0)) 
	dibujarReinas()

	if finDeJuego():
		TAMPANTALLA.blit(win,(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	else:

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				mousex,mousey = event.pos
	
				if clickEnCasilla(mousex,mousey):
	
					
					x = int((mousex - 10)/TAMCASILLA)
					y = int((mousey - 10)/TAMCASILLA)
	
					if x == 8:
						x = 7
					if y == 8:
						y = 7
	
					if movimientoLegal(x,y):
						invertirCasilla(x,y) 
					else:
	
						pygame.draw.rect(TAMPANTALLA, WHITE, (x*60 + 10,y*60 + 10,TAMCASILLA,TAMCASILLA))

	pygame.display.update()
	FPSCLOCK.tick(15)

