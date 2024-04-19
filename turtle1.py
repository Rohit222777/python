import turtle

# Create a turtle object
t = turtle.Turtle()

# Drawing a triangle
for _ in range(3):
    t.forward(100)  
    t.left(120)     

t.hideturtle()

turtle.done()