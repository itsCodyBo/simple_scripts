def main():
	
	return 0
if __name__ == '__main__':
	main()

#First import random
from random import randint

#create a list of the days of the week, then call using a random integer
week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

for x in week_days:
	i = randint(0,6)
	print week_days[i]
	break
	

#generates a number between 1-10 then returns the square in a string

rvalue = randint(1,10)
print 'The square of ' + str(rvalue) + ' is ' + str(rvalue*rvalue)
	
