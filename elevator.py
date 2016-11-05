import pygame

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
DARKGREY = (96, 96, 96)
RED = (255, 50, 50)
GREEN = (50, 255, 50)


class BaseRect(pygame.Rect):
	def __init__(self, pos_x, pos_y, width, height):
		super(BaseRect, self).__init__(pos_x, pos_y, width, height)


class ElevatorDoor(BaseRect):
	def __init__(self, pos_x, pos_y, width, height, side, elevator_speed):
		super(ElevatorDoor, self).__init__(pos_x, pos_y, width, height)
		self.speed = -1
		self._open_dist = 0
		self._elevator_speed = elevator_speed
		self.frame_offset = 5
		self.width = width / 2 - self.frame_offset
		self.height = height - 10

		self.x += self.frame_offset
		self.y += self.frame_offset

		if side == 'R':
			self.speed *= -1
			self.centerx += self.width

	def open(self):
		if self._open_dist != self.width:
			self._open_dist += abs(self.speed)
			print(self._open_dist, self.width)
			if self._open_dist < self.width:
				self.move_ip(self.speed, 0)
			else:
				self._open_dist = self.width

	def close(self):
		if self._open_dist != 0:
			self._open_dist -= abs(self.speed)
			print(self._open_dist, self.width)
			if self._open_dist > 0:
				self.move_ip(-self.speed, 0)
			else:
				self._open_dist = 0

	def up(self):
		self.move_ip(0, -self._elevator_speed)

	def down(self):
		self.move_ip(0, self._elevator_speed)


class ElevatorCabin(BaseRect):
	def __init__(self, pos_x, pos_y, width, height):
		super(ElevatorCabin, self).__init__(pos_x, pos_y, width, height)
		self.speed = 5
		self.left_door = ElevatorDoor(pos_x, pos_y, self.width, self.height, 'L', self.speed)
		self.right_door = ElevatorDoor(pos_x, pos_y, self.width, self.height, 'R', self.speed)

	def up(self, distance):
		while (distance - abs(self.speed)) != 0:
			self.move_ip(0, -self.speed)
			self.left_door.up()
			self.right_door.up()

	def down(self):
		self.move_ip(0, self.speed)
		self.left_door.down()
		self.right_door.down()


class Elevator(object):
	def __init__(self, pos_x, pos_y, surface):
		self.surface = surface
		self.pos_x = pos_x
		self.pos_y = pos_y

		self.cabin_w = 100
		self.cabin_h = 200
		self.cabin = ElevatorCabin(self.pos_x, self.pos_y, self.cabin_w, self.cabin_h)

		# Range
		self.floors = list(range(1, 11))
		self.max_height = 1000 - self.cabin.height
		self.floor_height = self.max_height / len(self.floors)
		self.draw()

	def draw(self):
		pygame.draw.rect(self.surface, GREY, self.cabin)
		pygame.draw.rect(self.surface, RED, self.cabin.left_door)
		pygame.draw.rect(self.surface, GREEN, self.cabin.right_door)

	def move_up(self, floor_num):
		print('Moving Up')
		if floor_num in self.floors:
			distance = self.floor_height * floor_num
			self.cabin.up(distance)

	def move_down(self, floor_num):
		print('Moving Down')
		self.cabin.down()

	def open_doors(self):
		print('Opening Doors')
		self.cabin.left_door.open()
		self.cabin.right_door.open()

	def close_doors(self):
		print('Closing Doors')
		self.cabin.left_door.close()
		self.cabin.right_door.close()
