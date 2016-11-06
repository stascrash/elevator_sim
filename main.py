import sys
import pygame
from elevator import Elevator
from world import Background
from controller import ElevatorMainControl, Passengers
pygame.init()

# COLORS
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARKGREY = (96, 96, 96)

# Game display
screen_width = 1024
screen_height = 768

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Elevator Simulator')
clock = pygame.time.Clock()

# background = Background(SIZE, 'data/images/tile_bg.png')

elevator = Elevator(screen)
elevator_height = screen_height / 10
elevator_width = elevator_height * 0.75
elevator.setup(100, screen_height - elevator_height, elevator_width, elevator_height, screen_height)
pygame.display.update()

move_up = False
move_down = False
doors = False
distance = 0
current_floor = 1
target_floor = 1
font = pygame.font.SysFont("None", 30)

def build_floors():
	cnt = 1
	for i in reversed(range(10)):
		y_pos = (screen_height / 10) * i
		text = font.render('Floor: {}'.format(cnt), True, RED)
		pygame.draw.rect(screen, DARKGREY, [0, y_pos, screen_width, 10])
		screen.blit(text, [10, y_pos+10])
		cnt += 1


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# get the floor
	if current_floor == target_floor:
		target_floor = Passengers.get_floor()
		# if target_floor == 10:
		# 	target_floor = 1
		# else:
		# 	target_floor = 10
		if current_floor + target_floor > 11:
			print("Requested same floor")
			target_floor = current_floor
			distance = 0
		else:
			current_pos = elevator.floor_height * current_floor - elevator.cabin_h + 1
			distance = abs((current_pos - elevator.floor_height * target_floor) + elevator.cabin_h - 1)

		print("Target Floor:", target_floor)
		if current_floor < target_floor:
			move_up = True
		elif current_floor > target_floor:
			move_down = True
		doors = True

	# Movements
	if move_up:
		go = False
		if elevator.doors_opened and doors:
			print('Doors are:', elevator.doors_opened)
			elevator.close_doors()
		else:
			go = True
			doors = False
		if go and not doors:
			if distance <= 0:
				go = False
			else:
				elevator.move_up()
				distance -= abs(elevator.cabin.speed)

		if not go and not doors:
			if not elevator.doors_opened:
				elevator.open_doors()
				print('Doors are:', elevator.doors_opened)
			else:
				move_up = False
				current_floor = target_floor

	if move_down:
		go = False
		if elevator.doors_opened and doors:
			print('Doors are:', elevator.doors_opened)
			elevator.close_doors()
		else:
			go = True
			doors = False
		if go and not doors:
			if distance <= 0:
				go = False
				doors = False
			else:
				elevator.move_down()
				distance -= abs(elevator.cabin.speed)
		if not go and not doors:
			if not elevator.doors_opened:
				elevator.open_doors()
				print('Doors are:', elevator.doors_opened)
			else:
				move_down = False
				current_floor = target_floor

	text = font.render('Next Floor: {}'.format(target_floor), True, RED)
	screen.fill(BLUE)
	build_floors()
	elevator.draw()
	screen.blit(text, (500,0))

	# Set FPS
	clock.tick(150)
	pygame.display.update()
