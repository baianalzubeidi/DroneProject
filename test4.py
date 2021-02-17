import pygame
from pygame.locals import *


pygame.init()

print("inti ")

while True:
    for event in pygame.event.get():
     # Detects the 'KEYDOWN' and 'KEYUP' events  
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):  
        # gets the key name  
            key_name = pygame.key.name(event.key)
            print(key_name)
        # converts to uppercase the key name  
            key_name = key_name.upper()  
        # if any key is pressed  
            if event.type == pygame.KEYDOWN:  
            # prints on the console the key pressed  
                print(u'"{}" key pressed'.format(key_name))  
        # if any key is released  
            elif event.type == pygame.KEYUP:  
            # prints on the console the released key  
                print(u'"{}" key released'.format(key_name))  