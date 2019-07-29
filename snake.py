import turtle
import random
UP_EDGE = 250
DOWN_EDGE= -250
RIGHT_EDGE= 400
LEFT_EDGE= -400
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)   
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()
def new_stamp():
	snake_pos=snake.pos()
	pos_list.append(snake_pos)
	q=snake.stamp()
	stamp_list.append(q)
for i in range(START_LENGTH):
	x_pos=snake.xcor()
	y_pos=snake.ycor()
	x_pos+=SQUARE_SIZE
	snake.goto(x_pos,y_pos)
	new_stamp()
print(pos_list)
def remove_tail():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
def up():
	snake.direction="Up"
	UP_EDGE = 250
	DOWN_EDGE= -250
	RIGHT_EDGE= 400
	LEFT_EDGE= -400
	print("You pressed the up key!")
def down():
    snake.direction="Down"
    print("You pressed the down key!")
def right():
    snake.direction="Right"
    print("You pressed the right key!")
def left():
    snake.direction="Left"
    print("You pressed the left key!")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.listen()
snake.direction="Right"
def move_snake():
	my_pos = snake.pos()
	x_pos = my_pos[0]
	y_pos = my_pos[1]
	if snake.direction == "Up":
		snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
	if snake.direction == "Down":
		snake.goto(x_pos, y_pos - SQUARE_SIZE)
	if snake.direction=="Right":
		snake.goto(x_pos+SQUARE_SIZE,y_pos)
	if snake.direction=="Left":
		snake.goto(x_pos-SQUARE_SIZE,y_pos)
   	new_stamp()
   	remove_tail()
	new_pos = snake.pos()
	new_x_pos = new_pos[0]
	new_y_pos = new_pos[1]
	if new_x_pos >= RIGHT_EDGE:
		print("You hit the right edge! Game over!")
		quit()
	elif new_x_pos <= LEFT_EDGE:
		print("You hit the right edge! Game over!")
		quit()
	elif new_y_pos >= UP_EDGE:
	    print("You hit the right edge! Game over!")
	    quit()
	elif new_y_pos <= DOWN_EDGE:
	    print("You hit the right edge! Game over!")
	    quit()
	turtle.ontimer(move_snake,TIME_STEP)
move_snake()







turtle.mainloop()
