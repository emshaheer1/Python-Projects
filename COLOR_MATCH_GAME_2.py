import turtle
import time
import random


delay = 0.01
col = ["red","green","blue","black"]
score = 0 
y = 3

#SET UP THE SCREEN
screen = turtle.Screen()
screen.title("Ihtisham")
screen.bgcolor()
screen.setup(1500,800)
screen.tracer(0)


#MOVING BOX
box = turtle.Turtle()
box.speed(0)
box.shapesize(1)
box.shape("circle")
box.color(random.choice(col))
box.penup()
box.goto(0, 130)
box.direction = "stop"


#BOTTOM BOX
bellow_box_1 = turtle.Turtle()
bellow_box_1.shapesize(0.5,6)
bellow_box_1.shape("square")
bellow_box_1.color("red")
bellow_box_1.penup()
bellow_box_1.goto(0,-250)

bellow_box_2 = turtle.Turtle()
bellow_box_2.shapesize(6,0.5)
bellow_box_2.shape("square")
bellow_box_2.color("blue")
bellow_box_2.penup()
bellow_box_2.goto(66,-315)

bellow_box_3 = turtle.Turtle()
bellow_box_3.shapesize(0.5,6)
bellow_box_3.shape("square")
bellow_box_3.color("green")
bellow_box_3.penup()
bellow_box_3.goto(0,-380)

bellow_box_4 = turtle.Turtle()
bellow_box_4.shapesize(6,0.5)
bellow_box_4.shape("square")
bellow_box_4.color("black")
bellow_box_4.penup()
bellow_box_4.goto(-66,-315)




#BLACK BORDERS
LEFT = turtle.Turtle()
LEFT.shapesize(50,0.5,3)
LEFT.shape("square")
LEFT.color("black")
LEFT.penup()
LEFT.goto(-300,0)

RIGHT = turtle.Turtle()
RIGHT.shapesize(50,0.5,3)
RIGHT.shape("square")
RIGHT.color("black")
RIGHT.penup()
RIGHT.goto(300,0)

#SCORE
scores = turtle.Turtle()
scores.speed(0)
scores.shape("square")
scores.color("red")
scores.penup()
scores.hideturtle()
scores.goto(0, 260)
scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal"))

def motion():
        box.direction = "down"

def moving_right():
    x1 = bellow_box_1.xcor()
    y1 = bellow_box_1.ycor()
    x2 = bellow_box_2.xcor()
    y2 = bellow_box_2.ycor()
    x3 = bellow_box_3.xcor()
    y3 = bellow_box_3.ycor()
    x4 = bellow_box_4.xcor()
    y4 = bellow_box_4.ycor()

    bellow_box_1.goto(x2,y2)
    bellow_box_2.goto(x3,y3)
    bellow_box_3.goto(x4,y4)
    bellow_box_4.goto(x1,y1)

    if x1 == 0:
        bellow_box_1.shapesize(6,0.5)
        bellow_box_2.shapesize(0.5,6)
        bellow_box_3.shapesize(6,0.5)
        bellow_box_4.shapesize(0.5,6)
    elif x1 == 66 or x1 == -66 :
        bellow_box_1.shapesize(0.5,6)
        bellow_box_2.shapesize(6,0.5)
        bellow_box_3.shapesize(0.5,6)
        bellow_box_4.shapesize(6,0.5)    


def moving_left():
    x1 = bellow_box_1.xcor()
    y1 = bellow_box_1.ycor()
    x2 = bellow_box_2.xcor()
    y2 = bellow_box_2.ycor()
    x3 = bellow_box_3.xcor()
    y3 = bellow_box_3.ycor()
    x4 = bellow_box_4.xcor()
    y4 = bellow_box_4.ycor()

    bellow_box_1.goto(x4,y4)
    bellow_box_2.goto(x1,y1)
    bellow_box_3.goto(x2,y2)
    bellow_box_4.goto(x3,y3)

    if x1 == 0:
        bellow_box_1.shapesize(6,0.5)
        bellow_box_2.shapesize(0.5,6)
        bellow_box_3.shapesize(6,0.5)
        bellow_box_4.shapesize(0.5,6) 
    elif x1 == 66 or x1 == -66 :
        bellow_box_1.shapesize(0.5,6)
        bellow_box_2.shapesize(6,0.5)
        bellow_box_3.shapesize(0.5,6)
        bellow_box_4.shapesize(6,0.5) 
        
                


screen.listen()
screen.onkeypress(motion, " ")
screen.onkeypress(moving_right, "Right")
screen.onkeypress(moving_left, "Left")

def move(x):
    if box.direction == "down":
        y = box.ycor() #y coordinate of the turtle
        box.sety(y - x)




while True:
    screen.update()

    if box.distance(bellow_box_1) <10:
        if box.color() == bellow_box_1.color():
            score = score + 1
            box.goto(0,130)
            scores.clear()    
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal"))
            box.color(random.choice(col))
            if score == 10 or score == 20 or score == 30 or score == 40 or score == 50 or score == 60 or score == 70:
                y = y + 1
        else:
            box.goto(0,130)
            score = 0
            scores.clear()    
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal")) 
            box.color(random.choice(col)) 
            box.direction = "stop" 
            y = 3
                   
    elif box.distance(bellow_box_2) <10:
        if box.color() == bellow_box_2.color():
            score = score + 1
            box.goto(0,130)
            scores.clear()
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal"))
            box.color(random.choice(col))
            if score == 10 or score == 20 or score == 30 or score == 40 or score == 50 or score == 60 or score == 70:
                y = y + 1
        else:
            box.goto(0,130)
            score = 0
            scores.clear()    
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal")) 
            box.color(random.choice(col))
            box.direction = "stop"  
            y = 3
 
    elif box.distance(bellow_box_3) <10:
        if box.color() == bellow_box_3.color():
            score = score + 1
            box.goto(0,130)
            scores.clear()
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal")) 
            box.color(random.choice(col))
            if score == 10 or score == 20 or score == 30 or score == 40 or score == 50 or score == 60 or score == 70:
                y = y + 1
        else:
            box.goto(0,130)
            score = 0
            scores.clear()    
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal")) 
            box.color(random.choice(col)) 
            box.direction = "stop"
            y = 3

    elif box.distance(bellow_box_4) <10:
        if box.color() == bellow_box_4.color():
            score = score + 1
            box.goto(0,130)
            scores.clear()
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal")) 
            box.color(random.choice(col))
            if score == 10 or score == 20 or score == 30 or score == 40 or score == 50 or score == 60 or score == 70:
                y = y + 1
        else:
            box.goto(0,130)
            score = 0
            scores.clear()    
            scores.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal")) 
            box.color(random.choice(col)) 
            box.direction = "stop"
            y = 3


        
    move(y)    

    time.sleep(delay)

screen.mainloop()
#turtle.done()