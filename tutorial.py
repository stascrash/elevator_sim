import sys
import numpy
import pygame
from pygame.locals import *
pygame.init()
# Assets
img = pygame.image.load('data/images/head.jpeg')
bg_img = pygame.image.load('data/images/tile_bg.png')
bg_pixels = pygame.surfarray.array2d(bg_img)
tile_bg_pixels = numpy.tile(bg_pixels, (7, 7)).astype(int)

size_X = bg_pixels.shape[0] * 7
size_Y = bg_pixels.shape[1] * 7

# Entry point setup
screen = pygame.display.set_mode((size_X, size_Y))
pygame.display.set_caption('Hello World')
colors = numpy.random.randint(0, 255, size=(4, 3))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)
clock = pygame.time.Clock()

steps = numpy.linspace(20, 360, 40).astype(int)
right = numpy.zeros((2, len(steps)))
down = numpy.zeros((2, len(steps)))
left = numpy.zeros((2, len(steps)))
up = numpy.zeros((2, len(steps)))

right[0] = steps
right[1] = 20
down[0] = 360
down[1] = steps
left[0] = steps[::-1]
left[1] = 360
up[0] = 20
up[1] = steps[::-1]

pos = numpy.concatenate((right.T, down.T, left.T, up.T))

clock.tick(30)



# Drawing basic Shapes
# pygame.draw.circle(screen, colors[0], (200, 200), 25, 0)
# pygame.draw.line(screen, colors[1], (0, 0), (200, 200), 3)
# pygame.draw.rect(screen, colors[2], (200, 0, 100, 100))
# pygame.draw.ellipse(screen, colors[3], (100, 200, 100, 50), 2)

font = pygame.font.SysFont('None', 50)

i = 0
while True:
	screen.fill(WHITE)
	pygame.surfarray.blit_array(screen, tile_bg_pixels)
	if i >= len(pos):
		i = 0
	screen.blit(img, pos[i])

	text = "{} {} {}".format(i, pos[i][0], pos[i][1])
	rendered = font.render(text, True, RED, BLUE)
	screen.blit(rendered, (10, 10))
	i += 1

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
