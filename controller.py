import random

class ElevatorMainControl(object):
	pass


class Passengers(object):

	@staticmethod
	def get_floor():
		return random.randrange(1, 9)
