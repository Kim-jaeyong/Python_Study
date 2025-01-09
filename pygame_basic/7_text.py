import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Yong's Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
obj = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/obj.png")
obj_size = obj.get_rect().size # 이미지의 크기를 구해옴
obj_width = obj_size[0] # 캐릭터의 가로 크기
obj_height = obj_size[1] # 캐릭터의 세로 크기
obj_x_pos = screen_width / 2  - obj_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
obj_y_pos = screen_height - obj_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 이동속도
obj_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2  - enemy_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 이벤트 루프
running = True # 게임이 진행중
while running:
  dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생하였는가
      running = False # 게임이 진행중이 아님

    if event.type == pygame.KEYDOWN: # 키가 눌러 졌는지 확인
        if event.key == pygame.K_LEFT: # 캐릭터를 왼족으로
            to_x -= obj_speed
        elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
            to_x += obj_speed
        elif event.key == pygame.K_UP: # 캐릭터를 위로
            to_y -= obj_speed
        elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
            to_y += obj_speed
    if event.type == pygame.KEYUP: # 키를 더이상 누르지 않음
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            to_y = 0
                
    obj_x_pos += to_x * dt
    obj_y_pos += to_y * dt
    
    # 가로 경계값 처리
    if obj_x_pos < 0:
        obj_x_pos = 0
    elif obj_x_pos > screen_width - obj_width:
        obj_x_pos = screen_width - obj_width        
    
    # 세로 경계값 처리a
    if obj_y_pos < 0:
        obj_y_pos = 0
    elif obj_y_pos > screen_height - obj_height:
        obj_y_pos = screen_height - obj_height
        
    # 충돌처리를 위한 rect 정보 업데이트
    obj_rect = obj.get_rect()
    obj_rect.left = obj_x_pos
    obj_rect.top = obj_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if obj_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False
    
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(obj, (obj_x_pos, obj_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어 초(s) 단위로 표시
    
    timer = game_font.render((str(int(total_time - elapsed_time))), True, (255, 255, 255))
    # render(text, antialias, color)
    screen.blit(timer, (10, 10))
    
    # 시간이 0 이하로 떨어지면 게임 종료
    if (total_time - elapsed_time) <= 0:
        print("타임 오버")
        running = False
    
    pygame.display.update() # while문을 돌며 계속 배경을 그려줌
    
# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기
    
# pygame 종료
pygame.quit()