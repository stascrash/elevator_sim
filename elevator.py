import pygame

WHITE = (255, 255, 255)
GREY = (128, 128, 128)


class ElevatorCabin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.image = pygame.Surface([100, 200])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)

		pygame.draw.rect(self.image, GREY, [0, 0, 100, 200])
		self.rect = self.image.get_rect()

	def move_up(self, pixels):
		self.rect.y -= pixels

	def move_down(self, pixels):
		self.rect.y += pixels
