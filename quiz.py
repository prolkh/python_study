import pygame
#######################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Old Game")  # 게임 이름

#FPS
clock = pygame.time.Clock()
#######################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load('D:/Python/myoracsil/background.png')

character = pygame.image.load('D:/Python/myoracsil/character.png')
character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

x_v = 1
x_a = 0

running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)                 # 게임 화면의 초당 프레임 수

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_a += 1
                x_v *= x_a
            elif event.key == pygame.K_RIGHT:
                x_a -= 1
                x_v *= -x_a
        
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += x_v


    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))



    pygame.display.update()

pygame.quit()

