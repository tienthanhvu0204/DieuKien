import turtle
shapeinput = input ("Circle and square, what is your favorite shape?: ")
if shapeinput == "circle" or shapeinput == "square":
    colorinput = input ("What color will it be?: ")
    if colorinput == "yellow" or colorinput == "red" or colorinput == "blue":
        screen = turtle.Screen ()
        screen.setup (1000, 1000)
        screen.title ("Your shape is " + shapeinput)
        screen.bgcolor ("#BDB76B")
        t = turtle.Turtle ()
        t.shape (shapeinput)
        t.color (colorinput)
        t.shapesize (5)
        turtle.done ()
    else:
        print ("Sorry, we don't have this color :(") 
else:
    print ("Sorry, we don't have this shape :(")
