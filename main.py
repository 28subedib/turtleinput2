import turtle
from random import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')
t = turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('White')
t.write("Background Colors",font=("arial",30,"normal"),align="center")
t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('Tan')
t.write("1. Tan",font=("arial",20,"normal"),align="left")
t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('Azure')
t.write("2. Azure",font=("arial",20,"normal"),align="left")
t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Aquamarine')
t.write("3. Aquamarine",font=("arial",20,"normal"),align="left")
t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('Darkkhaki')
t.write("4. Darkkhaki",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write("Choose a color",font=("arial",30,"normal"),align="center")

choose = int(input("Choose a color:"))
if choose == 1:
    screen.bgcolor("Tan")
elif choose == 2:
    screen.bgcolor("Azure")
elif choose == 3:
    screen.bgcolor("Aquamarine")
else:
    screen.bgcolor("Darkkhaki")
t.clear()

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("Enter your name",font=("arial",30,"normal"),align="center")
name = input("Enter your name: ")
t.clear()
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

import random

operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    #add
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution=num1+num2
elif operation == 2:
    symbol = "-"
    # subtract
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    solution = num1 - num2
elif operation == 3:
    symbol = "*"
    # multiply
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)

    solution = num1 * num2

elif operation == 4:
    symbol = "/"
    # divide
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)
    sign = random.randint(1,2)
    if sign == 2:
        num2 = -1*num2
    solution = num1 / num2



t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('blue')
t.write(name,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('red')
t.write(symbol,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('pink')
t.write(num1,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('hotpink')
t.write(num2,font=("arial",30,"normal"),align="center")


t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('red')
t.write('=',font=("arial",30,"normal"),align="center")
ans = float(input("Please enter your answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('purple')
t.write(solution,font=("arial",30,"normal"),align="center")
if ans == solution:
    screen.bgcolor("dodgerblue")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("Your answer is: "+str(ans),font=("arial",30,"normal"),align="center")

import turtle
import random
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))



sum = num1+num2



if ans == solution:
    screen.bgcolor('dodgerblue')


    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor('black')
    t.write("Correct"+str(ans),font=("arial",30,"normal"),align="center")

else:
    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor('black')
    t.write("Incorrect"+str(ans),font=("arial",30,"normal"),align="center")












turtle.done()
