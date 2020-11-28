import pygame


pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Old Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("D:/Python/myoracsil/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/Python/myoracsil/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해본다.
character_width = character_size[0]     # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2      # 화면 가로의 절반 크기에 위치 설정
character_y_pos = screen_height - character_height         # 화면 맨 아래 위치

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 이벤트 발생을 계속 받음
        if event.type == pygame.QUIT:   # 창닫기 버튼 이벤트 발생시
            running = False

    screen.blit(background, (0, 0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()

