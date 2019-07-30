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
def down():
    snake.direction="Down"
def right():
    snake.direction="Right"
def left():
    snake.direction="Left"
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.listen()
turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for this_food_pos in (food_pos):
    food.goto(this_food_pos)
    a=food.stamp()
    food_stamps.append(a)
    print(food_stamps)
    
snake.direction="Right"
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    if snake.direction == "Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    if snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
    if snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
    if snake.pos() in pos_list:
        quit()
    new_stamp()
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp'
        new_stamp()
        
        
        print("You have eaten the food!")
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
    if len(food_stamps) <=6:
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    a=food.stamp()
    food_stamps.append(a)
move_snake()







turtle.mainloop()
