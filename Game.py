import sys, pygame,os

pygame.init()
#######################
x = 40
y = 60

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
######################
size=width, height = 1280,600
screen=pygame.display.set_mode(size)

# Ball
ball=pygame.image.load("ball.gif")
ball=ball.convert()
ballrect=ball.get_rect()
ballrect=ballrect.move(560,280)
#

# Stick 1
stick=pygame.image.load("stick.png")
stick.convert()
stickrect=stick.get_rect()
stickrect=stickrect.move(1,240)
#

# Stick 2
stick2=pygame.image.load("stick2.png")
stick.convert()
stickrect2=stick2.get_rect()
stickrect2=stickrect2.move(1180,240)
#

black=(0,0,0)
white = (255,255,255)

end=pygame.image.load("end.jpg")
end=end.convert()
endrect=end.get_rect()

# Speed
speed=[1,1]
speedstc1=[0,0]
speedstc2=[0,0]
#


while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT : sys.exit()
			#########FOR STICK 2
		if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
			speedstc2[1]=-4
		if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
			speedstc2[1]=4
		if event.type==pygame.KEYUP:
			speedstc2[1]=0
		
			#########FOR STICK 1
		if event.type==pygame.KEYDOWN and event.key==pygame.K_z:
			speedstc1[1]=-4
		if event.type==pygame.KEYDOWN and event.key==pygame.K_x:
			speedstc1[1]=4
		if event.type==pygame.KEYUP:
			speedstc1[1]=0	

	stickrect=stickrect.move(speedstc1)
	stickrect2=stickrect2.move(speedstc2)
	ballrect=ballrect.move(speed)	
	
	
    ###########################
	if ballrect.collidelistall([stickrect]):
		speed[0]=-speed[0]
		
	if ballrect.collidelistall([stickrect2]):
		speed[0]=-speed[0]
		
	
	if ballrect.top<0 or ballrect.bottom>height:
		speed[1]=-speed[1]
		
	if ballrect.left < 0 or ballrect.right > width:
		break
	
	if stickrect.top<0 or stickrect.bottom>height:
		speedstc1=[0,0]
		
	if stickrect2.top<0 or stickrect2.bottom>height:
		speedstc2=[0,0]	
	
	
	
	
	screen.fill(black)	
	screen.blit(ball,ballrect)
	screen.blit(stick,stickrect)
	screen.blit(stick2,stickrect2)
	pygame.display.flip()


####################################################################
font=pygame.font.Font(None,36)
game = font.render("Game over :) - Tab to exit",1,(255,255,255))
gamerect=game.get_rect(left=20,top=100)
screen.blit(end,endrect)
screen.blit(game, gamerect)
pygame.display.flip()
while 1:
   for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()











