import pygame
import math

pygame.init()
screen_size = (1500,670)
surface_size = (25,45)

screen = pygame.display.set_mode(screen_size)
#surface = pygame.Surface()

pygame.display.set_caption("angry_bird_clone")

game_running = True

# textures init 
#bird_red_img = pygame.image.load("res\\bird_red.png")

# game data
dist = 0
player_cod = [200,300]
end_point= [0,0]
angle_sign = 1
angle = 0
x_comp = 0
y_comp = 0
pressed = False
release = False
gravity = 50 
clock = pygame.time.Clock()
current_duration = init_time = vel = 0
# game loop
while game_running:
    # checking for events
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    dist = math.sqrt(
        math.pow(
            mouse_pos[0] - player_cod[0],
            2
        )
        +
        math.pow(
            mouse_pos[1] - player_cod[1],
            2
        )        
    )
    hor_dist = math.sqrt(
        math.pow(
            player_cod[0] - mouse_pos[0],
            2
        )       
    )
    angle = math.acos(hor_dist/(dist+0.01))
    
    if mouse_pos[1] > player_cod[1]:
        angle_sign = +1
        angle *= +1
    else:
        angle_sign = -1
        angle *= -1
    

    screen.fill((0,0,0))
    #screen.blit(bird_red_img, player_cod)
    
      
    #pygame.draw.line(screen,(0,255,17),player_cod,mouse_pos,5)
    #pygame.draw.polygon(screen,(0,255,0),(player_cod,mouse_pos,(mouse_pos[0], player_cod[1])))
    #angle expression (in degrees) : math.degrees(math.atan(mouse_pos[0]/dist)) 
    if pygame.mouse.get_pressed()[2] == True:
        player_cod = list((mouse_pos[0]+1,mouse_pos[1]+1))
    if pygame.mouse.get_pressed()[0]:
        #pygame.draw.line(screen,(31,102,0),player_cod,mouse_pos,3)  
        if angle_sign == 1:
            pygame.draw.line(screen,(255,0,242),player_cod,(player_cod[0]+hor_dist,player_cod[1]+(player_cod[1]-mouse_pos[1])),3)
        
        elif angle_sign == -1:
            pygame.draw.line(screen,(255,0,242),player_cod,(player_cod[0]+hor_dist,player_cod[1]-(mouse_pos[1]-player_cod[1])),3)
        
    if pressed == False and pygame.mouse.get_pressed()[0] == True:
        pressed = True
        
    if pressed == True :
        #print(pygame.mouse.get_pressed()[0], release)
        if pygame.mouse.get_pressed()[0] == False:
            release = True
            pressed = False
            x_comp = dist * math.cos(angle)*0.09
            y_comp = dist * math.sin(angle)*0.15
            #print("x-comp : ", x_comp, " ","y-comp : ",y_comp)
            init_time = pygame.time.get_ticks()

    if release == True:

        current_duration = (pygame.time.get_ticks() - init_time)/1000
        init_pt_copy = list(player_cod)
        player_cod[0] += x_comp
        #(y_comp*current_duration - 0.5*9.8*current_duration**2)
        vel = (y_comp-gravity*current_duration)*0.5 
        player_cod[1] += -(vel) 
            
        #print(init_pt_copy[1] + (y_comp*current_duration - 0.5*9.8*current_duration**2))

    #print("y-velocity : ",vel,end='\r')
    
    pygame.draw.circle(screen,(0,255,0),player_cod,15)
    pygame.display.update()
    if keys[pygame.K_r]:
        dist = 0
        player_cod = [200,300]
        #end_point= [0,0]
        angle_sign = 1
        x_comp = 0
        y_comp = 0
        pressed = False
        release = False
        

print()
pygame.quit()
