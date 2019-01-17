import turtle

def draw_square(brad):
    for i in range(1,5) :
        brad.forward(100)
        brad.right(90)

def draw_triangle() :
    jenni = turtle.Turtle()
    jenni.penup()
    jenni.goto(100,30)
    jenni.pendown()
    jenni.shape("circle")
    jenni.color("green")
    for i in range(1,4) :
        jenni.forward(100)
        jenni.left(120)

def draw_circle() :
    angie = turtle.Turtle()
    angie.penup()
    angie.goto(50,50*1.73)
    angie.pendown()
    angie.shape("arrow")
    angie.color("blue")    
    angie.circle(50)    

def draw_shape3(brad) :
    brad.right(90)
    brad.forward(100)
    brad.backward(50)
    brad.left(45)
    brad.forward(75)
    brad.backward(75)
    brad.left(90)
    brad.forward(75)

    brad.right(45)
    brad.penup()
    brad.forward(100)
    brad.pendown()
    brad.forward(50)
    brad.backward(50)
    brad.right(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(50)

def my_goto(brad, x, y) :
    brad.penup()
    brad.goto(x, y)
    brad.pendown()

def draw_triangle2(brad, d) :
    brad.fill(True)
    for i in range(1,4) :
        brad.forward(d)
        brad.left(120)
    brad.fill(False)

def draw_shape2(brad) :
    brad.fill(True)
    tup = (0.1, 0.8, 0.25)
    brad.color("blue",tup)
    for i in range(1,4) :
        brad.forward(300)
        brad.left(120)
    brad.fill(False)
    brad.forward(150)
    
    tup = (1, 1, 1)
    brad.color("blue",tup)
    
    brad.left(60)
    draw_triangle2(brad, 150)

    my_goto(brad, 225, 0)
    draw_triangle2(brad, 75)

    #brad.right(60)
    my_goto(brad, 262.5, 0)    
    draw_triangle2(brad, 37.5)
    
    #brad.left(120)
    my_goto(brad, 187.5, 0)    
    draw_triangle2(brad, 37.5)

    my_goto(brad, 225, 64.95)    
    draw_triangle2(brad, 37.5)

    my_goto(brad, 75, 0)
    draw_triangle2(brad, 75)

    #brad.right(60)
    my_goto(brad, 112.5, 0)    
    draw_triangle2(brad, 37.5)
    
    #brad.left(120)
    my_goto(brad, 37.5, 0)    
    draw_triangle2(brad, 37.5)

    my_goto(brad, 75, 64.95)    
    draw_triangle2(brad, 37.5)

    my_goto(brad, 150, 129.90)
    draw_triangle2(brad, 75)

    #brad.right(60)
    my_goto(brad, 112.5, 129.90)    
    draw_triangle2(brad, 37.5)
    
    #brad.left(120)
    my_goto(brad, 187.5, 129.90)    
    draw_triangle2(brad, 37.5)

    my_goto(brad, 150, 129.90 + 64.95)    
    draw_triangle2(brad, 37.5)





def draw_shape():    
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(50)    
    #draw_square(brad)
    draw_shape2(brad)
    brad.right(60)
    my_goto(brad, -300, 150)
    draw_shape3(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(50)
    my_goto(angie, -150, -150)
    for i in range(1,37):
        angie.right(10)
        angie.circle(50)
    #draw_triangle()
    #draw_circle()
    



    window.exitonclick()
    
draw_shape()
