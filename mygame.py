import pygame
import random as rm
pygame.init()

#defining colours
white=(255, 255, 255)
red=(255,0,0)
black=(0,0,0)

#Adding snake personality
snake_height=7
snake_width=7

#defining time
clock=pygame.time.Clock()

#defining size fo the window
gameWindow=pygame.display.set_mode((900,700))

#set caption
pygame.display.set_caption("Kanna Game")
pygame.display.update()

#defining font
font=pygame.font.SysFont(None,30)

#display score
def display_text(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#plotting the snake
def plot_snake(gameWindow,color,snake_list,snake_width,snake_height):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_width,snake_height]) 

#defining homepage
def homepage():
    exit_game=False
    while exit_game!=True:
        gameWindow.fill((223,220,229))
        display_text('Welcome to snake game',black,300,300)
        display_text('Press Space to play',black,310,330)
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
                 exit_game=True
           if event.type==pygame.KEYDOWN:
              if event.key==pygame.K_SPACE:
                gameloop()
        pygame.display.update()
        clock.tick(30) 

#Gameloop
def gameloop():

    #Adding positions
    snake_x=35
    snake_y=55

    #game control options
    game_over=False
    exit_game=False

    #defining moves
    move_x=move_y=0

    #status
    status1=0
    status2=0

    #defining food
    food_x=rm.randint(20,450)
    food_y=rm.randint(160,450)

    #score initially 0
    score=0

    #Defining fps
    fps=30

    #snakelength and snakelist
    snake_list=[]
    snake_length=1

    #opening file
    with open('highscore.txt','r') as f:
        highscore=f.read()


    while(exit_game!=True):
        #Handling events in game
        if game_over:
            with open('highscore.txt','w') as f:
                   f.write(str(highscore))
            gameWindow.fill(black)
 
            display_text('Game Over! Press Enter to continue',red,250,280)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                       homepage()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT and status1==0:
                        move_x=4
                        move_y=0
                        status1=1
                        status2=0

                    if event.key==pygame.K_LEFT and status1==0:
                        move_x=-4
                        move_y=0
                        status1=1
                        status2=0

                    if event.key==pygame.K_UP and status2==0:
                        move_y=-4
                        move_x=0
                        status2=1
                        status1=0
                    if event.key==pygame.K_DOWN and status2==0:
                        move_y=4
                        move_x=0 
                        status2=1
                        status1=0 
        
            snake_x+=move_x
            snake_y+=move_y  
        
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6 :
                pygame.mixer.music.load('beep-07a.mp3')
                pygame.mixer.music.play()
                score+=10
                food_x=rm.randint(20,450)
                food_y=rm.randint(160,450)
                snake_length+=1
                if score>int(highscore):
                    highscore=score

            gameWindow.fill(black)
            display_text('Score: '+str(score)+'  Highscore: '+str(highscore),red,5,5)
            #creating food
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_width,snake_height])
            
            #creating snakehead
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
        
            #deleting snakehead
            if len(snake_list)>snake_length:
                del snake_list[0]

            #defining collision
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()    
            
            #defining gameover
            if(snake_x<0 or snake_x>900 or snake_y<0 or snake_y>700):
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                
           
    
            #plot snake 
            plot_snake(gameWindow,white,snake_list,snake_width,snake_height)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
homepage()
pygame.quit()
quit()


    
