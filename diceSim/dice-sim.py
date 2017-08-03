#dice generator

from random import randint
roll=randint(2,14)

def game(roll):
	if roll == 7 or roll==14:
		print "you lose"
	else:
		print "you win"
		
print roll
print game(roll)

