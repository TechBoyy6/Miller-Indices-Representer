import turtle

my_pen = turtle.Turtle()
tut = turtle.Screen() 
tut.bgcolor("black") 
tut.title("Miller Indices Representer") 
my_pen.speed(3)

def cube():
    my_pen.color("white")

    for i in range(4):
        my_pen.pendown()
        my_pen.forward(100)
        my_pen.left(90)

    my_pen.home()
    my_pen.penup()
    my_pen.goto(50, -50)
    my_pen.pendown()

    for i in range(4):
        my_pen.pendown()
        my_pen.forward(100)
        my_pen.left(90)

    my_pen.goto(0, 0)
    my_pen.goto(0, 100)
    my_pen.goto(50, 50)
    my_pen.goto(150, 50)
    my_pen.goto(100, 100)
    my_pen.goto(100, 0)
    my_pen.goto(150, -50)

def Negative_Axis():

    # X-axis
    my_pen.color("green", "green")
    my_pen.penup()
    my_pen.goto(150, 50)
    my_pen.pendown()
    my_pen.goto(220, 50)
    my_pen.begin_fill()
    my_pen.goto(210, 57)
    my_pen.goto(210, 43)
    my_pen.goto(220, 50)
    my_pen.end_fill()
    my_pen.write("X-axis", False, font=("Arial", 15, "bold"))
    my_pen.penup()

    # Y-axis
    my_pen.goto(150, 50)
    my_pen.pendown()
    my_pen.goto(150, 120)
    my_pen.begin_fill()
    my_pen.goto(143, 110)
    my_pen.goto(157, 110)
    my_pen.goto(150, 120)
    my_pen.end_fill()
    my_pen.write("Y-axis", False, font=("Arial", 15, "bold"))
    my_pen.penup()

    # Z-axis 
    my_pen.goto(150, 50)
    my_pen.pendown()
    my_pen.goto(185, 15)
    my_pen.begin_fill()
    my_pen.goto(188, 25)
    my_pen.goto(168, 25)
    my_pen.goto(185, 15)
    my_pen.end_fill()
    my_pen.penup()
    my_pen.goto(190, -5)
    my_pen.write("Z-axis", False, font=("Arial", 15, "bold"))


def Positive_Axis():

    # X-axis
    my_pen.color("green", "green")
    my_pen.penup()
    my_pen.goto(100, 0)
    my_pen.pendown()
    my_pen.goto(180, 0)
    my_pen.begin_fill()
    my_pen.goto(170, 7)
    my_pen.goto(170, -7)
    my_pen.goto(180, 0)
    my_pen.end_fill()
    my_pen.write("X-axis", False, font=("Arial", 15, "bold"))
    my_pen.penup()

    # Y-axis
    my_pen.goto(0, 100)
    my_pen.pendown()
    my_pen.goto(0, 170)
    my_pen.begin_fill()
    my_pen.goto(-7, 160)
    my_pen.goto(7, 160)
    my_pen.goto(0, 170)
    my_pen.end_fill()
    my_pen.write("Y-axis", False, font=("Arial", 15, "bold"))
    my_pen.penup()

    # Z-axis 
    my_pen.goto(50, -50)
    my_pen.pendown()
    my_pen.goto(85, -85)
    my_pen.begin_fill()
    my_pen.goto(72, -80)
    my_pen.goto(87, -80)
    my_pen.goto(85, -85)
    my_pen.end_fill()
    my_pen.penup()
    my_pen.goto(90, -80)
    my_pen.write("Z-axis", True, font=("Arial", 15, "bold"))


def Positive_Plot(x, y, z):

    miller_indices = [x, y, z]
    
    if miller_indices.count(0) == 0:
        # (111)
        my_pen.color("blue")
        my_pen.penup()
        my_pen.goto(100/x, 0)         # >> x
        my_pen.pendown()
        my_pen.goto(0, 100/y)         # >> y
        my_pen.goto(50/z, -50/z)        # >> z
        my_pen.goto(100/x, 0)

    elif miller_indices.count(0) == 1:

        if miller_indices.index(0) == 1:        # (101)
            my_pen.color("orange")
            my_pen.penup()
            my_pen.goto(100/x, 0)
            my_pen.pendown()
            my_pen.goto(50/z, -50/z)
            my_pen.goto(50/z, 100-(50/z))
            my_pen.goto(100/x, 100)
            my_pen.goto(100/x, 0)

        elif miller_indices.index(0) == 0:          # (011)
            my_pen.color("orange")
            my_pen.penup()
            my_pen.goto(0, 100/y)
            my_pen.pendown()
            my_pen.goto(100, 100/y)
            my_pen.goto(100+(50/z), -50/z)
            my_pen.goto(50/z, -50/z)
            my_pen.goto(0, 100/y)

        else:                                       # (110)
            my_pen.color("orange")
            my_pen.penup()
            my_pen.goto(0, 100/y)
            my_pen.pendown()
            my_pen.goto(50, (100/y)-50)
            my_pen.goto((100/x)+50, -50)
            my_pen.goto(100/x, 0)
            my_pen.goto(0, 100/y)

    else:
        if miller_indices[0] != 0:        # (100)
            my_pen.color("red")
            my_pen.penup()
            my_pen.goto(100/x, 0)
            my_pen.pendown()
            my_pen.goto(100/x, 100)
            my_pen.goto(50+(100/x), 50)
            my_pen.goto(50+(100/x), -50)
            my_pen.goto(100/x, 0)

        elif miller_indices[1] != 0:          # (010)
            my_pen.color("red")
            my_pen.penup()
            my_pen.goto(0, 100/y)
            my_pen.pendown()
            my_pen.goto(100, 100/y)
            my_pen.goto(150, (100/y)-50)
            my_pen.goto(50, (100/y)-50)
            my_pen.goto(0, 100/y)

        else:                                       # (001)
            my_pen.color("red")
            my_pen.penup()
            my_pen.goto(50/z, -50/z)
            my_pen.pendown()
            my_pen.goto(100+(50/z), -50/z)
            my_pen.goto(100+(50/z), 100-(50/z))
            my_pen.goto(50/z, 100-(50/z))
            my_pen.goto(50/z, -50/z)

def Negative_Plot(x, y, z):

    miller_indices = [x, y, z]

    if miller_indices.count(0) == 0:
        # (-1 -1 -1)
        my_pen.color("blue")
        my_pen.penup()
        my_pen.goto(150-(100/x), 50)         # >> x
        my_pen.pendown()
        my_pen.goto(150, 50-(100/y))         # >> y
        my_pen.goto(150-(50/z), 50+(50/z))        # >> z
        my_pen.goto(150-(100/x), 50)

    elif miller_indices.count(0) == 1:

        if miller_indices.index(0) == 1:        # (-1 0 -1)
            my_pen.color("orange")
            my_pen.penup()
            my_pen.goto(150-(100/x), 50)
            my_pen.pendown()
            my_pen.goto(150-(50/z), 50+(50/z))
            my_pen.goto(150-(50/z), -(50-(50/z)))
            my_pen.goto(150-(100/x), -50)
            my_pen.goto(150-(100/x), 50)

        elif miller_indices.index(0) == 0:          # (0 -1 -1)
            my_pen.color("orange")
            my_pen.penup()
            my_pen.goto(150, 50-(100/y))
            my_pen.pendown()
            my_pen.goto(100, 100/z)
            my_pen.goto(0, 100/z)
            my_pen.goto(50, 50-(100/y))
            my_pen.goto(150, 50-(100/y))

        else:                                       # (-1 -1 0)
            my_pen.color("orange")
            my_pen.goto(150-(100/x), 50)
            my_pen.pendown()
            my_pen.goto(150, 50-(100/y))
            my_pen.goto(100, 100-(100/y))
            my_pen.goto(100-(100/x), 100)
            my_pen.goto(150-(100/x), 50)

    else:
        if miller_indices[0] != 0:        # (-1 0 0)
            my_pen.color("red")
            my_pen.penup()
            my_pen.goto(150-(100/x), 50)
            my_pen.pendown()
            my_pen.goto(150-(100/x), -50)
            my_pen.goto(100-(100/x), 0)
            my_pen.goto(100-(100/x), 100)
            my_pen.goto(150-(100/x), 50)

        elif miller_indices[1] != 0:          # (0 -1 0)
            my_pen.color("red")
            my_pen.penup()
            my_pen.goto(150, 50-(100/y))
            my_pen.pendown()
            my_pen.goto(50, 50-(100/y))
            my_pen.goto(0, 100-(100/y))
            my_pen.goto(100, 100-(100/y))
            my_pen.goto(150, 50-(100/y))

        else:                                       # (0 0 -1)
            my_pen.color("red")
            my_pen.penup()
            my_pen.goto(150-(50/z), 50+(50/z))
            my_pen.pendown()
            my_pen.goto(50-(50/z), 50+(50/z))
            my_pen.goto(50-(50/z), -(50-(50/z)))
            my_pen.goto(100+50-(50/z), -(50-(50/z)))
            my_pen.goto(150-(50/z), 50+(50/z))

def clear():
    my_pen.clear()
    my_pen.penup()
    my_pen.home()




while True:

    validation = input("Press P for positive plot or N for negative plot\n>")

    if validation.lower() == "n":

        x = int(input("Provide the x intercept: "))
        y = int(input("Provide the y intercept: "))
        z = int(input("Provide the z intercept: "))

        clear()
        cube()
        Negative_Axis()
        Negative_Plot(-x, -y, -z)

    elif validation.lower() == "p":

        x = int(input("Provide the x intercept: "))
        y = int(input("Provide the y intercept: "))
        z = int(input("Provide the z intercept: "))

        clear()
        cube()
        Positive_Axis()
        Positive_Plot(x, y, z)

    else:
        print("Good Bye :)")
        break