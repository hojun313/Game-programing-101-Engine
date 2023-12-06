import pygame
import sys
import random
from Physics import Collision_Detection
from Physics import Rigid_Body_Dynamics
from Physics import Particle_System as Particle
from Audio import X_axis_Audio

# pygame 초기화
pygame.init()

# 화면 설정
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# 프로그램 이름
pygame.display.set_caption("Platformer")

# FPS
clock = pygame.time.Clock()
fps = 60

# 색깔
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)

# 플레이어 리지드 바디
player_rigid_body = Rigid_Body_Dynamics.RigidBody(100, 100, 50, 50, 0, 0, 1, 0.02)
player_friction_x = False

# 플레이어 점프
player_jump = False
player_jump_power = 35

# 지형 리지드 바디 리스트
terrain_rigid_body_list = [
    Rigid_Body_Dynamics.RigidBody(0, 900, 1100, 10),
    Rigid_Body_Dynamics.RigidBody(1200, 800, 600, 10),
    Rigid_Body_Dynamics.RigidBody(600, 600, 500, 10),
    Rigid_Body_Dynamics.RigidBody(0, 500, 500, 10),
    Rigid_Body_Dynamics.RigidBody(1200, 400, 400, 10),
    Rigid_Body_Dynamics.RigidBody(0, 200, 400, 10),
    Rigid_Body_Dynamics.RigidBody(1700, 200, 300, 10)
]

# 파티클 생성 함수
def create_particles(x, y):
    particles = []
    for _ in range(20):  # 파티클 개수 조절 가능
        particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        particles.append(Particle.Particle(x, y, 1, 7, 100, 200, 1, 0.01, particle_color))
    return particles

particles = []

# 메인 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        # 종료 이벤트
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 키보드 이벤트
        if event.type == pygame.KEYDOWN:
            # ESC 키
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE:
                player_jump = True

            if event.key == pygame.K_LEFT:
                player_rigid_body.velocity_x = -10

            if event.key == pygame.K_RIGHT:
                player_rigid_body.velocity_x = 10

    # 중력 적용
    player_rigid_body.apply_force(0, 4 * player_rigid_body.mass)

    # 플레이어 리지드 바디와 지형 리지드 바디 충돌 감지
    for terrain_rigid_body in terrain_rigid_body_list:
        player_rect_list = [player_rigid_body.x, player_rigid_body.y, player_rigid_body.width, player_rigid_body.height]
        terrain_rect_list = [terrain_rigid_body.x, terrain_rigid_body.y, terrain_rigid_body.width, terrain_rigid_body.height]
        if Collision_Detection.check_AABB_collision(player_rect_list, terrain_rect_list):
            # 플레이어 리지드 바디와 지형 리지드 바디 충돌 시 플레이어 리지드 바디의 위치를 조정
            player_rigid_body.y = terrain_rigid_body.y - player_rigid_body.height
            player_rigid_body.velocity_y = 0
            player_friction_x = True
            if player_jump:
                particles = create_particles(player_rigid_body.x + player_rigid_body.width / 2, player_rigid_body.y + player_rigid_body.height)
                player_rigid_body.apply_force(0, -player_jump_power)
                X_axis_Audio.play_audio_with_stereo("Audio_Samples\jump.mp3", player_rigid_body.x, screen_width)
                player_rigid_body.update()
                player_jump = False

    # 플레이어 리지드 바디 업데이트
    player_rigid_body.update(player_friction_x)

    player_friction_x = False

    # 파티클 업데이트
    for particle in particles:
        particle.move()

    # 화면 지우기
    screen.fill(black)

    # 지형 그리기
    for terrain_rigid_body in terrain_rigid_body_list:
        terrain_rect_list = [terrain_rigid_body.x, terrain_rigid_body.y, terrain_rigid_body.width, terrain_rigid_body.height]
        pygame.draw.rect(screen, white, terrain_rect_list)

    # 플레이어 그리기
    pygame.draw.rect(screen, red, player_rect_list)

    # 파티클 그리기
    for particle in particles:
        pygame.draw.circle(screen, particle.color + (particle.alpha,), (int(particle.x), int(particle.y)), int(particle.size))

    # 화면 업데이트
    pygame.display.update()
    clock.tick(fps)

# pygame 종료
pygame.quit()