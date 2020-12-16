import os
import math
file=open('Day10.txt').read()
space=file.split('\n')

locations=[]
xvalues=[]
yvalues=[]
y=-1
for line in space:
    x=-1
    y+=1
    for point in line:
        x+=1
        if point=='#':
            locations.append((x,y)) #holds the coordinates of each asteroid
        elif point=='.':
            continue

count=[]
for (x0,y0) in locations: #picks the next asteroid in the list
    lineofsight=[]
    for (x1,y1) in locations: #compares the location of the asteroid to the others
        if x1==x0 and y1==y0: #skips itself
            continue
        elif x1>x0: #accounts for asteroids on a line in the "positive" direction
            m=((y1-y0)/(x1-x0),'p')
            if m not in lineofsight:
                lineofsight.append(m)
        elif x1<x0: #accounts for asteroids on a line in the "negative" direction
            m=((y1-y0)/(x1-x0),'n')
            if m not in lineofsight:
                lineofsight.append(m)
        elif x1==x0: #accounts for asteroids stacked, in both directions
            if y1>y0:
                m='infinite,p'
                if m not in lineofsight:
                    lineofsight.append(m)
            elif y1<y0:
                m='infinite,n'
                if m not in lineofsight:
                    lineofsight.append(m)
    count.append(len(lineofsight)) #counts how many asteroids (x0,y0) can see
print('Number of Asteroids Seen:',max(count))
print('Location of Montioring Station:', locations[count.index(max(count))])

(x0,y0)=locations[count.index(max(count))]
rotations={}
for (x1,y1) in locations: #compares the location of the asteroid to the others
    if x1==x0 and y1==y0: #skips itself
        continue
    elif x1!=x0: #accounts for asteroids on a line in the "positive" direction
        radians=(math.atan((y1-y0)/(x1-x0))) #math.atan gives the angle
        if radians<0:
#            float(radians)
            radians=radians+3.141592653589
            rotations[(x1,y1)]=radians
        if radians>0:
            rotations[(x1,y1)]=radians
#    elif x1<x0: #accounts for asteroids on a line in the "negative" direction
#        radians=(math.atan((y1-y0)/(x1-x0)))
#        rotations[(x1,y1)]=radians
    elif x1==x0: #accounts for asteroids stacked, in both directions
        if y1>y0:
            radians=3.141592653589
            rotations[(x1,y1)]=radians
        elif y1<y0:
            radians=0
            rotations[(x1,y1)]=radians
print(sorted(rotations))
