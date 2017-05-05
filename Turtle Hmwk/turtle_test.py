def main():
	
	return 0
if __name__ == '__main__':
	main()
#turtle smiley page


#imagine turtle starting at (0,0) on the x-y plane
import turtle 

x = raw_input("Enter h,w,c!:")


		
#this is the smiley face drawing
if x=="c":
		turtle.fillcolor('yellow')
		turtle.begin_fill()
		turtle.circle(150)
		turtle.end_fill()
		turtle.penup()
		turtle.forward(100)
		turtle.lt(90)
		turtle.forward(150)
		turtle.pendown()
		turtle.circle(100,-180)
		turtle.penup()
		turtle.bk(85)
		turtle.pendown()
		turtle.fillcolor('blue')
		turtle.begin_fill()
		turtle.circle(30)
		turtle.end_fill()
		turtle.penup()
		turtle.forward(30)
		turtle.lt(90)
		turtle.forward(150)
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(30)
		turtle.end_fill()

#This is the frowning face
elif x=='w':
	turtle.fillcolor('yellow')
	turtle.begin_fill()
	turtle.circle(150)
	turtle.end_fill()
	turtle.penup()
	turtle.forward(100)
	turtle.lt(90)
	turtle.forward(150)
	turtle.pendown()
	turtle.lt(135)
	turtle.forward(50)
	turtle.rt(90)
	turtle.forward(50)
	turtle.lt(90)
	turtle.forward(50)
	turtle.rt(90)
	turtle.forward(50)
	turtle.lt(90)
	turtle.forward(50)
	turtle.rt(90)
	turtle.forward(50)
	turtle.rt(45)
	turtle.penup()
	turtle.forward(100)
	turtle.rt(90)
	turtle.forward(75)
	turtle.pendown()
	turtle.fillcolor('red')
	turtle.begin_fill()
	turtle.circle(-30)
	turtle.end_fill()
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(-30)
	turtle.end_fill()

#this is the color changing face
elif x=='h':
	turtle.fillcolor('green')
	turtle.begin_fill()
	turtle.circle(150)
	turtle.end_fill()
	turtle.penup()
	turtle.forward(100)
	turtle.lt(90)
	turtle.forward(150)
	turtle.pendown()
	turtle.lt(135)
	turtle.forward(50)
	turtle.rt(90)
	turtle.forward(50)
	turtle.lt(90)
	turtle.forward(50)
	turtle.rt(90)
	turtle.forward(50)
	turtle.lt(90)
	turtle.forward(50)
	turtle.rt(90)
	turtle.forward(50)
	turtle.rt(45)
	turtle.penup()
	turtle.forward(100)
	turtle.rt(90)
	turtle.forward(75)
	turtle.pendown()
	turtle.fillcolor('orange')
	turtle.begin_fill()
	turtle.circle(-30)
	turtle.end_fill()
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(-30)
	turtle.end_fill()

else:
	print "Not a correct input!"	

