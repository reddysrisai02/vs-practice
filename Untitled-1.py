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
marble = sphere(pos=vector(0, 1, -1), radius=mRadius, color=color.red)

deltax = 0.3
deltay = 0.3
deltaz = 0.3

xPos = 0
yPos = 1
zPos = -1

while True:
    rate(10)
    xPos = xPos + deltax
    yPos = yPos + deltay
    zPos = zPos + deltaz
    
    xrme = xPos + mRadius
    xlme = xPos - mRadius
    ytme = yPos + mRadius
    ybme = yPos - mRadius
    zbme = zPos - mRadius
    zfme = zPos + mRadius

    Rwe = roomWidth/2 - wallThickness/2
    Lwe = -roomWidth/2 + wallThickness/2
    Cwe = roomHeight/2 - wallThickness/2
    Fwe = -roomHeight/2 + wallThickness/2
    Bwe = -roomDepth/2 + wallThickness/2
    Fwe = roomDepth/2 + wallThickness/2
    
    if xrme >= Rwe or xlme <= Lwe:
        deltax = -deltax
    if ytme >= Cwe or ybme <= Fwe:
        deltay = -deltay
    if zfme >= Fwe or zbme <= Bwe:
        deltaz = -deltaz
        
    marble.pos = vector(xPos, yPos, zPos)
