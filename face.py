#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

import turtle

turtle.setworldcoordinates(0,0,1000,1000)
turtle.bgcolor("black")
bob = turtle.Turtle() #like Ross

bob.begin_fill()
bob.color("lime green")
bob.left(90)
for x in range(2):
  bob.forward(300)
  bob.right(90)
  bob.forward(1000)
  bob.right(90)
bob.end_fill()

bob.penup()
bob.goto(0, 300)
bob.pendown()

bob.begin_fill()
bob.color("dark blue")
for x in range(2):
  bob.forward(700)
  bob.right(90)
  bob.forward(1000)
  bob.right(90)
bob.end_fill()

bob.penup()
bob.goto(850, 650)
bob.pendown()

sunset = ["dark orchid", "light coral", "tomato", "dark orange", "yellow"]
counter = 5
for x in sunset:
  bob.begin_fill()
  bob.color(x)
  bob.circle(55*counter+ (counter*counter // 10) * 50)
  counter = counter - 1
  bob.end_fill()
  bob.penup()
  xpos, ypos = bob.pos()
  bob.goto(xpos-45, ypos-10)
  bob.pendown()


turtle.done()