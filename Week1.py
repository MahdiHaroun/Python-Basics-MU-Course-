str_seconds = input("please enter the number of seconds ")
total_seconds=int(str_seconds)
hours= total_seconds//3600
secs_still_rem =total_seconds % 3600
minutes = secs_still_rem // 60 
secs_finally_remaining= secs_still_rem % 60
print ("hrs=", hours , "mins=" , minutes , "sec=" , secs_finally_remaining)
#****************

#x ="hello" 
#y= "blyet"
#a = len(x) + len(y)
#print(a)
#b = len("hello") + len ("blyet")
#print(b)
'''****************************************'''
import turtle   # use turtle libarry
wn = turtle.Screen()   # create the graphics window
blyet= turtle.Turtle()  # crated a turtle named blyet
blyet.forward(150)    # moving commands ==^^
blyet.left(90)
blyet.backward(150)
blyet.right(90)
blyet.backward(150)
blyet.left(90)
blyet.forward(150)
blyet.salary=500    #you can give some varibales and print them
print(blyet.salary)
'''**************************************'''
import turtle
wn = turtle.Screen()
suka= turtle.Turtle()
suka.forward(150)
suka.left(45)
suka.forward(150)
suka.right(45)
suka.backward(150)
suka.left(45)
suka.backward(150)
'''**************************************'''
import turtle
wn = turtle.Screen()
nakhoi = turtle.Turtle()
nakhoi.color("red")
nakhoi.forward(300)
nakhoi.left(45)
nakhoi.backward(300)
nakhoi.color("green")
nakhoi.right(45)
nakhoi.backward(150)
nakhoi.left(135)
nakhoi.forward(300)
nakhoi.color("purple")
nakhoi.left(45)
nakhoi.backward(300)
nakhoi.left(90)
nakhoi.backward(300)
nakhoi.left(45)
nakhoi.forward(200)
nakhoi.right(135)
nakhoi.forward(150)
'''***************************************'''
import turtle 
wn= turtle.Screen()
wn.bgcolor("lightgreen")
elan = turtle.Turtle()
elan.color("red")
elan.shape("arrow")
elan.up() # this will make the turtle moves without making a constant line after every move
distance = 5

for x in range (30) :
    elan.stamp() # this will copy the turtle on the every command 
    elan.forward(distance)
    elan.right(24)
    distance = distance + 2
wn.exitonclick()