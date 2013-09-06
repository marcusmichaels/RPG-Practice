
from character import *

class Enemy(Character):
	def __init__(self, name, hp, pwr):
		Character.__init__(self, name, hp, pwr)