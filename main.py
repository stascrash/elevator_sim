import sys
import pygame
from elevator import ElevatorCabin
from world import Background
pygame.init()

# COLORS
RED = (255, 0, 0)

# Game display
SIZE = (1024, 768)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Elevator Simulator')
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

background = Background(SIZE, 'data/images/bg_tile.jpg')

# Sprite setup
elevator = ElevatorCabin()
elevator.rect.x = 200
elevator.rect.y = 200

sprites.add(elevator)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		elevator.move_up(10)
	if keys[pygame.K_DOWN]:
		elevator.move_down(10)

	sprites.update()

	screen.fill(RED)
	pygame.surfarray.blit_array(screen, background.tiled_pixels)

	# elevator draw
	sprites.draw(screen)
	pygame.display.flip()

	# Set FPS
	clock.tick(30)

	pygame.display.update()