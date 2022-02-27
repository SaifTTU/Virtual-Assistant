import pygame, sys, os

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() # initiates pygame

pygame.display.set_caption('Visual Assistant')
animFrame = 0
WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
display = pygame.Surface((WINDOW_SIZE[0]*5,WINDOW_SIZE[1]*5))

global animation_frames
animation_frames = {}

def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 1
    for frame in frame_durations:
        animation_frame_id = animation_name + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        # player_animations/idle/idle_0.png
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame
        

animation_database = {}
animation_database['orbStart'] = load_animation('images/orbStart',[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5000])
state = 'orbStart' #animation state
rect = pygame.Rect(WINDOW_SIZE[0]/.85,150,0,0)

font = pygame.font.Font('freesansbold.ttf', 96)
green = (0, 0, 0) #b3e5fc
blue = (179, 229, 252)
text = font.render('Welcome to Crystal Virtual Assistant', True, blue, green)
textRect = text.get_rect()
textRect.center = (WINDOW_SIZE[0] * 2.5, WINDOW_SIZE[1] // 5)

questionText = font.render("", True, blue, green)

asked = False

totalFrames = 0

while True:



    text = font.render('Welcome to Crystal Virtual Assistant', True, blue, green)
    display.fill((146,244,255)) # clear screen by filling it with blue

    animFrame += 1
    totalFrames+=1
    if animFrame >= len(animation_database[state]): #if animation frame is larger than the max size of the current animation
        animFrame = 0
    currtimageID = animation_database[state][animFrame]
    currImage = animation_frames[currtimageID]
    display.blit(currImage,(rect.x,rect.y))
    display.blit(text, textRect)


    if(totalFrames>450 and asked == False):
        questionText = font.render("Listening...", True, blue, green)
        textRect2 = questionText.get_rect()
        textRect2.center = (WINDOW_SIZE[0] * 2, WINDOW_SIZE[1] * 4)
        display.blit(questionText, textRect2)
    if(asked==False and totalFrames > 500):
        asked = True
        command = input("Enter your command: ")
        questionText = font.render(command, True, blue, green)
        textRect2 = questionText.get_rect()
        textRect2.center = (WINDOW_SIZE[0] * 2, WINDOW_SIZE[1] * 4)
    if(asked==True):
        display.blit(questionText, textRect2)

    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
