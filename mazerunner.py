import pygame, sys
from pygame.locals import *
import maze

import random
from random import randint

NEGRO    = (   0,   0,   0) 
BLANCO    = ( 255, 255, 255) 
AZUL     = (   0,   0, 255)
VERDE     = (   0,  255, 0)
VELOCIDAD = 5
COL =False

class Corredor(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el protagonista. """
 
    #Establecemos el vector velocidad
    cambio_x = 0
    cambio_y = 0
    paredes = None
     
    # Funcion Constructor 

    def __init__(self, x, y):
        #  Llama al constructor padre
        pygame.sprite.Sprite.__init__(self)
  
        # Establecemos el alto y largo
        self.image = pygame.Surface([8, 8])
        self.image.fill(BLANCO)
 
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
     
    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. """
        self.cambio_x += x
        self.cambio_y += y
        
    def update(self):
        """ Cambia la velocidad del protagonista. """
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
        global COL
        COL = False
        #  Hemos chocado contra la pared despues de esta actualizacion?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            #Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            else:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
            COL = True
            
        # Desplazar arriba/izquierda
        self.rect.y += self.cambio_y
          
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False) 
        for bloque in lista_impactos_bloques:
                 
            # Reseteamos nuestra posicion basandonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            else:
                self.rect.top = bloque.rect.bottom     
            COL = True
            
class Obstaculo(pygame.sprite.Sprite):
    """ Pared con la que el protagonista puede encontrarse. """
    def __init__(self, x, y, largo, alto):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        #  Llama al constructor padre
        pygame.sprite.Sprite.__init__(self)
 
        # Construye una pared azul con las dimensiones especificadas por los parametros
        self.image = pygame.Surface([21, 21])
        self.image.fill(AZUL)
 
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x   


class Pieza_magica(pygame.sprite.Sprite):
    """ Pared con la que el protagonista puede encontrarse. """
    def __init__(self, x, y, largo, alto):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        #  Llama al constructor padre
        pygame.sprite.Sprite.__init__(self)
 
        # Construye una pared azul con las dimensiones especificadas por los parametros
        self.image = pygame.Surface([21, 21])
        self.image.fill(VERDE)
 
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x   






MAZE= maze.matriz



pygame.init()
screen = pygame.display.set_mode((861,861))

map_width = 2541
map_height = 2541
main_map = pygame.Surface((map_width, map_height))
main_map = main_map.convert()	

# Lista que almacena todos los sprites
total_sprites = pygame.sprite.Group()
 
# Construimos las paredes. (x_pos, y_pos, largo, alto)
pared_list = pygame.sprite.Group()

for i in xrange(0,121):
	for j in xrange(0,121):
		if MAZE[i][j]=='X':
			obs = Obstaculo((i*21)+1,(j*21)+1,10,600)
			pared_list.add(obs)
			total_sprites.add(obs)

corredor = Corredor(300, 300)
corredor.paredes = pared_list



total_sprites.add(corredor)
	

posx_pieza=randint(0,121)
posy_pieza=randint(0,121)
 
pieza = Pieza_magica((posx_pieza*21)+1,(posy_pieza*21)+1,21,21)

total_sprites.add(pieza)

reloj = pygame.time.Clock()
 
hecho = False

map_x = 0 # Only this should change
map_y = 0


def draw():
	total_sprites.update()
	main_map.fill(NEGRO)
	total_sprites.draw(main_map)    
draw()




screen.blit(main_map,(map_x, map_y, 861, 861))
pygame.display.flip() 



while not hecho:
	


	for evento in pygame.event.get():  

		if evento.type == pygame.QUIT:
			hecho = True
 
		elif evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_LEFT:
				corredor.cambiovelocidad(-(VELOCIDAD),0)
			elif evento.key == pygame.K_RIGHT:
				corredor.cambiovelocidad(VELOCIDAD,0)
			elif evento.key == pygame.K_UP:
				corredor.cambiovelocidad(0,-(VELOCIDAD))
			elif evento.key == pygame.K_DOWN:
				corredor.cambiovelocidad(0,VELOCIDAD)
                 
		elif evento.type == pygame.KEYUP:
			if evento.key == pygame.K_LEFT:
            	
				corredor.cambiovelocidad(VELOCIDAD,0)
                
			elif evento.key == pygame.K_RIGHT:
				corredor.cambiovelocidad(-(VELOCIDAD),0)
			elif evento.key == pygame.K_UP:
				corredor.cambiovelocidad(0,VELOCIDAD)
			elif evento.key == pygame.K_DOWN:
				corredor.cambiovelocidad(0,-(VELOCIDAD))

	

	key_pressed = pygame.key.get_pressed()
	if key_pressed[K_LEFT]:
		if not COL:
			map_x +=VELOCIDAD	

	if key_pressed[K_RIGHT]:
		if not COL:
			map_x -=VELOCIDAD
			

	if key_pressed[K_UP]: 
		if not COL:
			map_y += VELOCIDAD
	if key_pressed[K_DOWN]:
		if not COL:
			map_y -= VELOCIDAD
    

	if map_x > 0:
		map_x = 0
	if map_x < -(map_width-861):
		map_x = -(map_width-861)
	if map_y > 0:
		map_y = 0		
	if map_y < -(map_height-861):
		map_y = -(map_height-861)

	draw()
	

	screen.blit(main_map,(map_x, map_y, 861, 861))
	pygame.display.flip() 
	reloj.tick(60)
             
pygame.quit()


