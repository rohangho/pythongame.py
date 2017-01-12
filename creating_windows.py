import pygame
import time
import random
#initialize

pygame.init()
display_width=800
display_height=600

#display the color in the screen in form of RGB
black = (0,0,0)
white = (255,255,255)

car_width=170

#set the display and it's resolution
gameDisplay = pygame.display.set_mode((display_width,display_height))

#it set the name of the title
pygame.display.set_caption('A Test Case')

#gives time
clock = pygame.time.Clock()

#load the car image
carImg=pygame.image.load('MY_car.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    


#display the image of the car
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
#coordinate of the place where the car will be displayed

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',49)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    
def crash():
    message_display('You asshole , you are busted')

def game_loop():

    x = (display_width*0.40)
    y = (display_height*0.56)

    x_change = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    dodged = 0


    #it starts only if the car is not crashed
    gameExit = False

    # game loop start
    while not gameExit:
        #pygame.event deals with any event occuring in screen like the mouse click in window or any thing else
        for event in pygame.event.get():
            #moves the car left and right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

    

        x += x_change

        
        #first the display the we have to call the car
        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        #it will exit if the car run boundary
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged +=1
            
        if y < thing_starty+thing_height:
            print('y coordinate crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        #it update the display
        pygame.display.update()

        #gives 61 frame per second means it will go through the loop 61 frames pre second
        clock.tick(61)

game_loop()
pygame.quit()
quit()

            
    

