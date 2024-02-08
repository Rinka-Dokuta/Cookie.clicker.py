#gopher mash
#written by Dr. Mo, 11/10/2020
#Updated by Manuel Romero, 2/8/2024
import pygame
import math #needed for square root function


#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0
isBig = False

pygame.init()#initializes Pygame
print(pygame.font.get_fonts())
pygame.display.set_caption("Cookie Clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen
CookiePic = pygame.image.load("COOKIE.png")#Loads cookie
CookieRect = CookiePic.get_rect(topleft=(100, 100))
CookiePic2 = pygame.image.load("COOKIE2.png")#Loads bigger cookie
CookieRect2 = CookiePic2.get_rect(topleft=(30,30))
font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('score:', False, (0, 200, 200))
text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
pygame.mixer.music.load("Minecraft.mp3")#Remove if file not found
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


print(pygame.font.get_fonts())

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 194
circY = 195
radius = 100

#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
        if math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2)<radius:#Distance Formula
            numClicks+=1
            print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
        if math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2)<radius:
            isBig = True
        else:
            isBig = False
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    
    if isBig == False:
        screen.blit(CookiePic, CookieRect)#If mouse not over cookie then cookie small
    else:
        screen.blit(CookiePic2, CookieRect2)#Else if mouse over cookie then cookie big
    
    
    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (110, 10))
    
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()
