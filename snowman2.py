# Rudy Sanchez Assignment 2

import turtle
wn = turtle.Screen()
wn.bgcolor("blue")

# FUNCTION DRAW A GENERAL CIRCLE
def draw_circle(r, name, px, angle, x, y, line_color, fill_color, pen_size):
    name = turtle.Turtle()
    name.color(line_color, fill_color)
    name.pensize(pen_size)
    name.up()
    name.goto(x, y)
    name.down()
    name.hideturtle()
    name.speed(0)
    name.begin_fill()
    for i in range(r):
        name.forward(px)
        name.left(angle)
    name.end_fill()

# FUNCTION TO DRAW A GENERAL LINE
def draw_line(name, start_x, start_y, end_x, end_y, line_color, pen_size):
    name = turtle.Turtle()
    name.color(line_color)
    name.pensize(pen_size)
    name.up()
    name.goto(start_x, start_y)
    name.down()
    name.hideturtle()
    name.speed(0)
    name.goto(end_x, end_y)

# BODY
draw_circle(360, 'body_mid', 2, 1.15, 0, 0, 'black', 'white', 1)
draw_circle(360, 'body_top', 1, 1, 0, 200, 'black', 'white', 1)
draw_circle(360, 'body_bottom',3, 1.25, 0, -275, 'black', 'white', 1)
draw_circle(360, 'button_one', .15, 1, 0, 55, 'black', 'red', 1)
draw_circle(360, 'button_two', .15, 1, 0, 85, 'black', 'red', 1)
draw_circle(360, 'button_three', .15, 1, 0, 115, 'black', 'red', 1)
draw_circle(360, 'button_two', .15, 1, 0, 145, 'black', 'red', 1)
draw_circle(360, 'left_eye', .15, 1, -25, 265, 'black', 'black', 1)
draw_circle(360, 'right_eye', .15, 1, 25, 265, 'black', 'black', 1)

# NOSE
draw_line('nose_top_right', 0, 265, 10, 265, 'orange', 4)
draw_line('nose_top_left', 0, 265, -10, 265, 'orange', 4)
draw_line('nose_right', 10, 265, 0, 235, 'orange', 3)
draw_line('nose_left', -10, 265, 0, 235, 'orange', 3)

# ARMS AND FINGERS
draw_line('arm_right', 102, 90, 205, 90, 'black', 8)
draw_line('arm_left', -102, 90, -205, 90, 'black', 8)
draw_line('finger_right_one', 205, 90, 195, 105, 'black', 5)
draw_line('finger_right_two', 205, 90, 215, 105, 'black', 5)
draw_line('finger_right_three', 205, 90, 220, 90, 'black', 5)
draw_line('finger_right_four', 205, 90, 215, 75, 'black', 5)
draw_line('finger_right_five', 205, 90, 195, 75, 'black', 5)
draw_line('finger_left_one', -205, 90, -195, 105, 'black', 5)
draw_line('finger_left_two', -205, 90, -215, 105, 'black', 5)
draw_line('finger_left_three', -205, 90, -220, 90, 'black', 5)
draw_line('finger_left_four', -205, 90, -215, 75, 'black', 5)
draw_line('finger_left_five', -205, 90, -195, 75, 'black', 5)

# HAT
hat = turtle.Turtle()
hat.color('black', 'white')
hat.pensize(10)
hat.up()
hat.goto(0, 315)
hat.down()
hat.hideturtle()
hat.begin_fill()
hat.forward(65)
hat.left(90)
hat.forward(10)
hat.left(90)
hat.forward(35)
hat.right(90)
hat.forward(65)
hat.left(90)
hat.forward(60)
hat.left(90)
hat.forward(65)
hat.right(90)
hat.forward(35)
hat.left(90)
hat.forward(10)
hat.left(90)
hat.forward(65)
hat.end_fill()

# TREES
def draw_trunk(name):     # draw a trunk
    for i in range(2):
        name.forward(50)
        name.left(90)
        name.forward(75)
        name.left(90)

def draw_tree(name):        # draw the branches
    for i in range(3):
        name.forward(80)
        name.left(120)


left_tree = turtle.Turtle()  # left tree trunk
left_tree.pensize(3)
left_tree.color('brown')
left_tree.up()
left_tree.goto(-250, 150)
left_tree.down()
left_tree.hideturtle()
left_tree.begin_fill()
draw_trunk(left_tree)   # call to draw trunk function
left_tree.end_fill()

right_tree = turtle.Turtle()  # right tree trunk
right_tree.pensize(3)
right_tree.color('brown')
right_tree.up()
right_tree.goto(250, 150)
right_tree.down()
right_tree.hideturtle()
right_tree.begin_fill()
draw_trunk(right_tree)  # call to draw trunk function
right_tree.end_fill()

left_tree_branch = turtle.Turtle()
left_tree_branch.pensize(3)
left_tree_branch.color('green')
left_tree_branch.up()
left_tree_branch.goto(-265, 225)
left_tree_branch.down()
left_tree_branch.hideturtle()
left_tree_branch.begin_fill()
draw_tree(left_tree_branch)   # call to draw tree function
left_tree_branch.end_fill()

right_tree_branch = turtle.Turtle()
right_tree_branch.pensize(3)
right_tree_branch.color('green')
right_tree_branch.up()
right_tree_branch.goto(235, 225)
right_tree_branch.down()
right_tree_branch.hideturtle()
right_tree_branch.begin_fill()
draw_tree(right_tree_branch)   # call to draw tree function
right_tree_branch.end_fill()

wn.exitonclick()