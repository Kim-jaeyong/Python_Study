import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Yong's Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
obj = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/obj.png")
obj_size = obj.get_rect().size # 이미지의 크기를 구해옴
obj_width = obj_size[0] # 캐릭터의 가로 크기
obj_height = obj_size[1] # 캐릭터의 세로 크기
obj_x_pos = screen_width / 2  - obj_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
obj_y_pos = screen_height - obj_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프
running = True # 게임이 진행중
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생하였는가
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(obj, (obj_x_pos, obj_y_pos)) # 캐릭터 그리기
    
    pygame.display.update() # while문을 돌며 계속 배경을 그려줌
    

    
# pygame 종료
pygame.quit()