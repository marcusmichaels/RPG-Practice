
from character import *

class Player(Character):
	def __init__(self, name, hp, pwr, intl):
		Character.__init__(self, name, hp, pwr)
		self.intl = intl