from vpython import *

mRadius = 0.75
wallThickness = 0.1
roomWidth = 15
roomDepth = 12
roomHeight = 8

# Create floor, ceiling, walls, and marble objects
floor = box(pos=vector(0, -roomHeight/2, 0), size=vector(roomWidth, wallThickness, roomDepth), color=color.red)
ceiling = box(pos=vector(0, roomHeight/2, 0), size=vector(roomWidth, wallThickness, roomDepth), color=color.blue) 
backwall = box(pos=vector(0, 0, -roomDepth/2), size=vector(roomWidth, roomHeight, wallThickness), color=color.green)
leftwall = box(pos=vector(-roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
rightwall = box(pos=vector(roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white) 
marble = sphere(radius=mRadius, color=color.red)

deltax = 0.1
xPos = 0

while True:
    rate(10)
    xPos = xPos + deltax
    xrem = xPos + mRadius
    xlme = xPos - mRadius
    Rwe = roomWidth/2 - wallThickness/2
    Lwe = -roomWidth/2 + wallThickness/2  # Corrected the calculation for Lwe
    if xrem > Rwe or xlme < Lwe:  # Corrected variable name 'roomWidth' to 'roomWidth/2'
        deltax = deltax * (-1)
    marble.pos = vector(xPos, 0, 0)  # Use 'pos' instead of 'Pos'
