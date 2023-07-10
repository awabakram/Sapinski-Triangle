import turtle
import random


#Scaler is for size of triangle
scaler = 1000
#Offset is for how much you want the triangle shifted from (0,0)
offset = 500
#dotSize for size of the dots
dotSize = 5

#initial_coordinates = [(0,0), (scaler, 0), (scaler/2, scaler * 0.866)]
initial_coordinates = [(0 - offset,0 - offset), (scaler - offset, 0 - offset), ((scaler/2) - offset, (scaler * 0.866) - offset)]

#Initial setup of the turtle
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

#Draw teh intital triangle points
for coord in initial_coordinates:
    turtle.setpos(coord[0],coord[1])
    turtle.dot(dotSize,"black")

#set and draw the first point
coord2 = (0,-67)
turtle.setpos(coord[0],coord[1])
turtle.dot(dotSize,"black")

#main loop
while True:
    coord1 = initial_coordinates[random.randint(0,2)]
    coord2 = ((coord1[0]+coord2[0])/2,(coord1[1]+coord2[1])/2)
    turtle.setpos(coord2[0],coord2[1])
    turtle.dot(dotSize,"black")
    
turtle.done()
