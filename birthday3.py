import turtle

my_turtle_cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
y_coordinate = -140


def draw_candle_for_cake_1(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()
 
def draw_stick_on_candle_1(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update() 
    

   
def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

my_turtle_screen.bgcolor("white")

parts_of_cake = []
parts_of_cake.append(["#ff5233", "#000000", 3, 60])
parts_of_cake.append(["white", "#000000", 3, 40])
parts_of_cake.append(["#ff5233", "#000000", 3, 60])

draw_layer_of_the_cake("orange", "#000000", 3, -220, y_coordinate - 70, 400, 10)

for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
    y_coordinate += parts[3]
   


draw_candle_for_cake_1("#8714e1", "#000000", -25, y_coordinate - 60)
draw_stick_on_candle_1("red", -11, y_coordinate + 15, 7)



turtle.done()