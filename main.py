import pygame,sys,random
from pygame.locals import*
#loads pygame so we can use it
pygame.init()
screen_info = pygame.display.Info()

#set width and height to the size of the screen
size = (width,height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
#create clock object used to control refresh rate
clock = pygame.time.Clock()
#creates color with RGB
color = (0,127,255)

#load fish image and rect
fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image, (80,80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width//2,height//2)

#set fish speed and rotation
speed = pygame.math.Vector2(0,10)
rotation = random.randint(0,360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image,180-rotation)

#create function to move fish
def move_fish():
  #makes fish_image a global variable
  global fish_image
  screen_info = pygame.display.Info()
  fish_rect.move_ip(speed)
  #if x coordinates of fish surpass the walls
  if fish_rect.left < 0 or fish_rect.right > screen_info.current_w:
    #flip the vector
    speed[0]*=-1
    #flip the image
    fish_image = pygame.transform.flip(fish_image,True,False)
    #moves so doesn't get stuck
    fish_rect.move_ip(speed[0],0)
  if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
    speed[1]*=-1
    fish_image = pygame.transform.flip(fish_image,False,True)
    fish_rect.move_ip(0,speed[1])

#creates main function
def main():
  #infinite while loop
  while True:
    #sets maximum refresh rate
    clock.tick(60)
    #calls move_fish function
    move_fish()
    #sets background color
    screen.fill(color)
    #adds the fish to the screen
    screen.blit(fish_image,fish_rect)
    #updates the contents of the entire display
    pygame.display.flip()

#calls main funciton after checking that the built in variable __name__ is equal to __main__
if __name__ == "__main__":
  main()
