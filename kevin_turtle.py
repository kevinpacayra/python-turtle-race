import time
import turtle
from turtle import *
from random import randint

window = turtle.Screen()
window.title("Python Turtle Race")
turtle.bgcolor("hotpink")
turtle.speed(0) # The speed of our turtle
turtle.penup()  # This will make turtle lines invisible
turtle.setpos(-330, 200) # This will position our turtle
turtle.write("Python Turtle Race", font = ("Arial", 10, "bold"))
turtle.penup()

turtle.setpos(-800, -220)
turtle.color("black")
turtle.begin_fill()
turtle.pendown()
turtle.forward(1300)
turtle.right(100)
turtle.forward(600)
turtle.right(100)
turtle.forward(1300)
turtle.right(100)
turtle.forward(600)
turtle.end_fill()

turtle.setpos(1800, 153)

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("white")
turtle1.shape("turtle")
turtle1.penup()
turtle1.setheading(90)
turtle1.setpos(-190, -240)

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("yellow")
turtle2.shape("turtle")
turtle2.penup()
turtle2.setheading(90)
turtle2.setpos(-140, -240)

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("red")
turtle3.shape("turtle")
turtle3.penup()
turtle3.setheading(90)
turtle3.setpos(-90, -240)

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("green")
turtle4.shape("turtle")
turtle4.penup()
turtle4.setheading(90)
turtle4.setpos(-40, -240)

turtle5 = Turtle()
turtle5.speed(0)
turtle5.color("cyan")
turtle5.shape("turtle")
turtle5.penup()
turtle5.setheading(90)
turtle5.setpos(10, -240)

turtle6 = Turtle()
turtle6.speed(0)
turtle6.color("blue")
turtle6.shape("turtle")
turtle6.penup()
turtle6.setheading(90)
turtle6.setpos(60, -240)

turtle7 = Turtle()
turtle7.speed(0)
turtle7.color("gray")
turtle7.shape("turtle")
turtle7.penup()
turtle7.setheading(90)
turtle7.setpos(110, -240)

turtle8 = Turtle()
turtle8.speed(0)
turtle8.color("indigo")
turtle8.shape("turtle")
turtle8.penup()
turtle8.setheading(90)
turtle8.setpos(160, -240)

time.sleep(1)

a = ""
turtle.penup()
turtle.goto(-250, -200)
turtle.write(a)
addk = 0
addkk = 0
addkkk = 0
addkkkk = 0
addkkkkk = 0
addkkkkkk = 0
addkkkkkkk = 0
addkkkkkkkk = 0

for i in range(220):
    a = randint(1, 8)
    b = randint(1, 8)
    c = randint(1, 8)
    d = randint(1, 8)
    e = randint(1, 8)
    f = randint(1, 8)
    g = randint(1, 8)
    h = randint(1, 8)
    turtle1.forward(a)
    turtle2.forward(b)
    turtle3.forward(c)
    turtle4.forward(d)
    turtle5.forward(e)
    turtle6.forward(f)
    turtle7.forward(g)
    turtle8.forward(h)

    addk += a
    addkk += b
    addkkk += c
    addkkkk += d
    addkkkkk += e
    addkkkkkk += f
    addkkkkkkk += g
    addkkkkkkkk += h

    if addk >= 401:
      print("winner is turtle 1")
      b = "winner is turtle 1"
      turtle.write(b, font=("Arial", 16, "bold"))
      break
    elif addkk >= 401:
      print("winner is turtle 2")
      c = "winner is turtle 2"
      turtle.write(c, font=("Arial", 16, "bold"))
      break
    elif addkkk >= 401:
      print("winner is turtle 3")
      d = "winner is turtle 3"
      turtle.write(d, font=("Arial", 16, "bold"))
      break
    elif addkkkk >= 401:
      print("winner is turtle 4")
      e = "winner is turtle 4"
      turtle.write(e, font=("Arial", 16, "bold"))
      break
    elif addkkkkk >= 401:
      print("winner is turtle 5")
      f = "winner is turtle 5"
      turtle.write(f, font=("Arial", 16, "bold"))
      break
    elif addkkkkkkk >= 401:
      print("winner is turtle 6")
      g = "winner is turtle 6"
      turtle.write(g, font=("Arial", 16, "bold"))
      break
    elif addkkkkk >= 401:
      print("winner is turtle 7")
      h = "winner is turtle 7"
      turtle.write(h, font=("Arial", 16, "bold"))
      break
    elif addkkkkk >= 401:
      print("winner is turtle 8")
      i = "winner is turtle 8"
      turtle.write(i, font=("Arial", 16, "bold"))
      break

turtle.exitonclick()

















    
    
