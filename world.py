import pygame
import numpy


class Background(object):
	def __init__(self, size, img_path):
		bg_img = pygame.image.load(img_path)
		bg_pixels = pygame.surfarray.array2d(bg_img)
		tile_x = size[0] / bg_pixels.shape[0]
		tile_y = size[1] / bg_pixels.shape[1]
		self.tiled_pixels = numpy.tile(bg_pixels, (tile_x, tile_y)).astype(int)
