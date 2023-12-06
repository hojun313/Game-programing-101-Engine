import pygame

# 초기화
pygame.init()

# 화면 크기 및 제목 설정
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("맵 편집기")

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 타일 크기 및 색상
TILE_SIZE = 50

# 맵 데이터
map_data = []
for i in range((SCREEN_HEIGHT // TILE_SIZE) + 1):
    map_data.append([0] * ((SCREEN_WIDTH // TILE_SIZE) + 1))

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 위치를 타일 좌표로 변환
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tile_x = mouse_x // TILE_SIZE
            tile_y = mouse_y // TILE_SIZE

            # 왼쪽 버튼 클릭시 벽 생성, 오른쪽 버튼 클릭시 빈 공간 생성
            if event.button == 1:
                map_data[tile_y][tile_x] = 1
            elif event.button == 3:
                map_data[tile_y][tile_x] = 0
        elif event.type == pygame.KEYDOWN:
            # 스페이스바를 누르면 종료
            if event.key == pygame.K_SPACE:
                running = False

    # 화면 초기화
    screen.fill(WHITE)

    # 맵 그리기
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # 화면 업데이트
    pygame.display.flip()

# 맵 데이터 저장
with open("Design\Maps\map_data.txt", "w") as f:
    for row in map_data:
        for tile in row:
            f.write(str(tile))
        f.write("\n")

# 게임 종료
pygame.quit()
