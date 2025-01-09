import pygame
from random import *

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()

# 배경 화면 불러오기
background = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/background.png")

# 스프라이트 불러오기
# 멋쟁이 주인공 재용
obj = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/obj.png")
obj_size = obj.get_rect().size
obj_width = obj_size[0]
obj_height = obj_size[1]
obj_x_pos = (screen_width / 2) - (obj_width / 2)
obj_y_pos = screen_height - obj_height

# 채라 똥
poop = pygame.image.load("C:/Users/용/Desktop/PythonWorkSpace/pygame_basic/poop.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = randint(0, 410)
poop_y_pos = 0

# 주인공이 움직일 X 좌표 및 이동속도
obj_to_x_left= 0
obj_to_x_right = 0
obj_speed = 300

# 똥이 내려오는 속도
poop_speed = 700

running = True
while running:
	dt = clock.tick(30) / 1000# 게임 화면의 초당 프레임 수를 설정
 
	# 2. 이벤트 처리 (키보드, 마우스 등)
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False 
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				obj_to_x_left = -obj_speed
			if event.key == pygame.K_RIGHT:
				obj_to_x_right = obj_speed

		# 키를 더이상 누르지 않음
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
					obj_to_x_left = 0
			elif event.key == pygame.K_RIGHT:
					obj_to_x_right = 0
				
	obj_x_pos += (obj_to_x_left + obj_to_x_right) * dt
	
	if obj_x_pos <= 0:
		obj_x_pos = 0
	elif obj_x_pos > screen_width - 70:
		obj_x_pos = screen_width - 70

	poop_y_pos += poop_speed * dt

	if poop_y_pos > (screen_height - poop_height):
		poop_x_pos = randint(0, 480 - poop_width)
		poop_y_pos = 0
		
	# 4. 충돌 처리
	# rect 정보 업데이트
	obj_rect = obj.get_rect()
	obj_rect.left = obj_x_pos
	obj_rect.top = obj_y_pos
	
	poop_rect = poop.get_rect()
	poop_rect.left = poop_x_pos
	poop_rect.top = poop_y_pos
	
	if obj_rect.colliderect(poop_rect):
		print("충돌")
		running = False
	 
	# 5. 화면에 그리기
	screen.blit(background, (0,0))
	screen.blit(obj, (obj_x_pos, obj_y_pos))
	screen.blit(poop, (poop_x_pos, poop_y_pos))
	pygame.display.update() # while문을 돌며 계속 배경을 그려줌

pygame.time.delay(2000)

# pygame 종료
pygame.quit()