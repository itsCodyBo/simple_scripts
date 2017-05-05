#dice generator

from random import randint
roll=randint(2,14)

def game(roll):
	answer=raw_input("do you want to roll? (type yes or no)")
	if answer=="yes":
		if roll == 7 or roll==14:
			print "you lose"
		else:
			print "you win"
	elif answer=="no":
		print "Fine, go away"
	else:
		print "type yes or no"
		
print roll
print game(roll)

