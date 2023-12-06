import random
import math

class Particle:
    def __init__(self, x, y, min_size, max_size, min_life, max_life, initial_speed, acceleration, color, alpha=255):
        self.x = x
        self.y = y
        self.size = random.uniform(min_size, max_size)
        self.life = random.uniform(min_life, max_life)
        self.initial_life = self.life
        self.initial_speed = initial_speed
        self.acceleration = acceleration
        self.color = color
        self.alpha = alpha

    def move(self):
        self.life -= 1
        if self.life > 0:
            self.x += self.initial_speed * math.cos(random.uniform(0, 2 * 3.14159))
            self.y += self.initial_speed * math.sin(random.uniform(0, 2 * 3.14159))
            self.initial_speed += self.acceleration
            self.alpha = int(255 * self.life / self.initial_life)

# 테스트 코드
if __name__ == "__main__":
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    particles = []
    for _ in range(100):
        particles.append(Particle(200, 200, 1, 5, 100, 200, 0.1, 0.01, (255, 0, 0)))

    while True:
        screen.fill((0, 0, 0))

        for particle in particles:
            particle.move()
            pygame.draw.circle(screen, particle.color + (particle.alpha,), (int(particle.x), int(particle.y)), int(particle.size))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()