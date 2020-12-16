import os
file=open('Day3.txt').read()
wire=file.split('\n')

wire1=wire[0] #reads the first line of the input as the first wire
wirelist1=wire1.split(',')
wire2=wire[1] #reads the second line of the input as the second wire
wirelist2=wire2.split(',')
#creates a list for the coordinates where the wires change directions
wirepath1=[(0,0)]
wirepath2=[(0,0)]

x=0
y=0
for turn in wirelist1:
    dir=turn[0]
    if dir=='R':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            x+=1
            wirepath1.append((x,y))
            move+=1
    elif dir=='L':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            x-=1
            wirepath1.append((x,y))
            move+=1
    elif dir=='U':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            y+=1
            wirepath1.append((x,y))
            move+=1
    elif dir=='D':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            y-=1
            wirepath1.append((x,y))
            move+=1

x=0
y=0
for turn in wirelist2:
    dir=turn[0]
    if dir=='R':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            x+=1
            wirepath2.append((x,y))
            move+=1
    elif dir=='L':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            x-=1
            wirepath2.append((x,y))
            move+=1
    elif dir=='U':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            y+=1
            wirepath2.append((x,y))
            move+=1
    elif dir=='D':
        dist=turn[1:]
        dist=int(dist)
        move=1
        while move<=dist:
            y-=1
            wirepath2.append((x,y))
            move+=1

coordset1=set(wirepath1)
coordset2=set(wirepath2)
overlaplist=list(coordset1 & coordset2)
ManhattanDistance=[]
for (x,y) in overlaplist:
    ManhattanDistance.append(abs(x)+abs(y))
ManhattanDistance.remove(0)
print('Manhattan Distance:', min(ManhattanDistance))

stepcount=[]
for coordinate in overlaplist:
    step1=wirepath1.index(coordinate)
    step2=wirepath2.index(coordinate)
    stepcount.append(step1+step2)
stepcount.remove(0)
print('Minimum Number of Steps:', min(stepcount))
