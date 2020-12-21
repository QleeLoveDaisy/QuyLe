import pygame, sys, random

#def draw_floor(): 
    #screen.blit(floor_surface,(floor_x_pos,900))
    #screen.blit(floor_surface,(floor_x_pos+576,900))
#Ham tao cai ong
def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 400)) #Tao cot o tren khoang cach 400
	return bottom_pipe,top_pipe
#Lam cho cot di chuyen
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes
#Tao ra cac cot random
def draw_pipes(pipes): 
     for pipe in pipes:
         if pipe.bottom>=1024:
             screen.blit(pipe_surface,pipe)
         else:
             flip_pipe=pygame.transform.flip(pipe_surface,False,True) #Tao cho ong tren giong ong duoi
             screen.blit(flip_pipe,pipe)
  #Kiem tra va cham          
def check_conlision(pipes):
       for pipe in pipes:
           if bird_rect.colliderect(pipe):  #Colliderect laf event va cham trong pygame
               return False

       if bird_rect.top <= -100 or bird_rect.bottom >= 900: #Neu bay len cao qua hoac thap qua cung chet
           return False

       return True

#Hoat anh cua chu chim
def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird,-bird_movement * 3,1) #*3, *4, gi cung dc
	return new_bird
#
def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
	return new_bird,new_bird_rect
#Ham tinh diem
def score_display(game_state):
	if game_state == 'main_game':
		score_surface = game_font.render(str(int(score)),True,(255,255,255))
		score_rect = score_surface.get_rect(center = (288,100))
		screen.blit(score_surface,score_rect)
	if game_state == 'game_over':
		score_surface = game_font.render(f'Score: {int(score)}' ,True,(255,255,255)) #f' dung man hinh
		score_rect = score_surface.get_rect(center = (288,100))
		screen.blit(score_surface,score_rect)

		high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
		high_score_rect = high_score_surface.get_rect(center = (288,780))  # 288,850
		screen.blit(high_score_surface,high_score_rect)
#Cap nhat diem
def update_score(score, high_score):
	if score > high_score:
		high_score = score
	return high_score

###
pygame.init()
screen=pygame.display.set_mode((576,1024)) # Tao ra man hinh 
#screen=pygame.display.set_mode((576,800))
clock=pygame.time.Clock()
#game_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf',50)
#game_font = pygame.font.Font('Font/UTM Ambrose.ttf',40)
game_font = pygame.font.Font('Font/UTM Alexander.ttf',50)
##Cac gia tri cua game

gravity=0.25 #Gia tri ma con chim bi rot xuong
bird_movement=0
game_active=True
score=0
high_score=0
#Cho surface 
bg_surface=pygame.image.load('assets/background-day.png').convert() #background cua game
bg_surface=pygame.transform.scale2x(bg_surface)  # de fit vua man hinh, du van de la (0,0)
# Cho floor
floor_surface=pygame.image.load('assets/base.png').convert()
floor_surface=pygame.transform.scale2x(floor_surface) 
floor_x_pos=0
#Cho con chim
bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))# Hinh chu nhat chua chu chim
#Su dung EVENT lam hoat anh cho canh con chim
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)
#bird_surface=pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
#bird_surface=pygame.transform.scale2x(bird_surface) 
#bird_rect=bird_surface.get_rect(center=(100,512))
# Hinh anh Cho cai Ong
pipe_surface=pygame.image.load('assets/pipe-green.png').convert()
pipe_surface=pygame.transform.scale2x(pipe_surface) 
pipe_list=[]
SPAWNPIPE=pygame.USEREVENT #set_timer(Ham su kien,1200ms
pygame.time.set_timer(SPAWNPIPE,1200) #Lien tuc tao su kien (La cai cot trong game) 
pipe_height=[400,600,800]

#Tao man hinh ket thuc Game
game_over_surface=pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha()) #phai la alpha moi dc man hinh

game_over_rect=game_over_surface.get_rect(center=(288,512))


while True:
    #Hinh anh cua nguoi choi
    # Hinh background
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type==pygame.KEYDOWN:  #Su kien de an phim cach chim bay len
          if event.key==pygame.K_SPACE:
              bird_movement=0
              bird_movement-=11     #Bam dau cach chim bay len
          if event.key==pygame.K_SPACE and game_active==False:
              game_active=True
              pipe_list.clear()
              bird_rect.center=(100,512)  #Khi ma no chet thi vi tri bat dau lai game la ntn
              bird_movement=0 #Phai co cai nay ko no rot xuong
              score=0    # Reset score, de score cao nhat dc giu lai, khong de score=high score(Luu diem)
       if event.type==SPAWNPIPE:
           pipe_list.extend(create_pipe()) #Goi cai ham tao pipe ra
       if event.type==BIRDFLAP:  #birddown la 0, mid la 1, up la 2
           if bird_index<2:
               bird_index+=1
           else:
                bird_index=0
           birbird_surface,bird_rect=bird_animation()

    
         

    screen.blit(bg_surface,(0,0)) #Goi de tao man hinh
    if game_active:
     #Bird
     bird_movement+=gravity
     rotated_bird = rotate_bird(bird_surface) #Goi ra hoat anh
     bird_rect.centery+=bird_movement
     screen.blit(rotated_bird,bird_rect)
     game_active=check_conlision(pipe_list) #Goi check_conllision
    #Pipes
     pipe_list=move_pipes(pipe_list)
     draw_pipes(pipe_list)
     score+=0.01 #Cong 0.01
     score_display('main_game') #Goi ham tinh diem
    else:
        #Ket thuc
        screen.blit(game_over_surface,game_over_rect) #Man hinh ket thuc
        high_score=update_score(score,high_score)
        score_display('game_over')

    

  
    #Floor
    #floor_x_pos-=1
    #draw_floor()
    #if floor_x_pos<=-576:
        #floor_x_pos=0

   
    pygame.display.update()
    clock.tick(120)  # 120 khung hinh 1 s

# 1 display surface co nhieu surface con o trong











