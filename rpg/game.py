
# Main game file

from characters.player import *
from commands import *
from utilities.util import *

def help(player, args):
	for command in commands:
		print command

commands = {
	'help': help,
	'exit': exit,
	'quit': exit
}

player = Player("Default", 1, 1, 1)

def nameInput(prompt):
	name = raw_input(prompt)

	return name.strip()

def getName():

	tempName = ""

	while 1:
		tempName = nameInput("What is your name? ")

		if len(tempName) < 1:
			continue

		yes = yesOrNo(tempName + ", is that your name?")

		if yes:
			return tempName
		else:
			continue


def isValidCMD(cmd):
	if cmd in commands:
		return True
	return False

def runCMD(cmd, args, player):
	commands[cmd](player, args)


def main(player):

	player.name = getName()

	while (not player.dead):
		line = raw_input(">> ")
		input = line.split()
		input.append("EOI")

		if isValidCMD(input[0]):
			runCMD(input[0], input[1], player)

main(player)