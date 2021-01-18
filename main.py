import turtle

avelina = turtle.Turtle()
avelina.shape('turtle')

avelina.penup()
avelina.begin_fill()
avelina.color('#e75480') #pink
avelina.goto(30,-15)
avelina.pendown() #line must seee
avelina.circle(130)

avelina.penup() #line not seen
avelina.end_fill() #pink color background
avelina.color('white')
avelina.goto(-10,150) #small circles coordinates.


avelina.pendown()#circle line visible
avelina.circle(20)
avelina.begin_fill()
avelina.color("blue")
avelina.circle(10)
avelina.end_fill()

#2nd eyes of fe at 120 
avelina.penup()
avelina.forward(70)
avelina.right(45)

avelina.pendown()
avelina.color('white')
avelina.circle(30)
avelina.begin_fill()
avelina.color('#FF000') #red
avelina.circle(10)
avelina.end_fill()


#go down
avelina.penup()
avelina.right(90)
avelina.forward(100)


avelina.pendown()
avelina.begin_fill()
avelina.color('#00FF00')
avelina.circle(40)
avelina.end_fill()

avelina.penup()
avelina.color('brown')
avelina.goto(30,120)





