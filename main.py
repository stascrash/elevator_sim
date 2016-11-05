import sys
import pygame
from elevator import Elevator
from world import Background
pygame.init()

# COLORS
BLUE = (0, 0, 255)

# Game display
SIZE = (1024, 768)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Elevator Simulator')
clock = pygame.time.Clock()

background = Background(SIZE, 'data/images/tile_bg.png')

elevator = Elevator(100, 550, screen)
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				elevator.move_up(4)
			elif event.key == pygame.K_DOWN:
				elevator.move_down(3)

	# keys = pygame.key.get_pressed()
	# if keys[pygame.K_UP]:
	# 	elevator.move_up(4)
	# if keys[pygame.K_DOWN]:
	# 	elevator.move_down(3)
	#
	# if keys[pygame.K_LEFT]:
	# 	elevator.open_doors()
	# if keys[pygame.K_RIGHT]:
	# 	elevator.close_doors()

	screen.fill(BLUE)

	elevator.draw()
	# pygame.surfarray.blit_array(screen, background.tiled_pixels)

	# Set FPS
	clock.tick(30)

	pygame.display.update()
