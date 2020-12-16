import os
file=open('Day1.txt').read()
mass=file.split()
fuel1=[]
fuel2=[]

for i in range(0,len(mass)):
    mass[i]=int(mass[i])
    fuel1.append(mass[i]//3-2)

print('Fuel Requirements (not counting fuel):',sum(fuel1))

for i in fuel1:
    while (i>0):
        i=i//3-2
        if i>0:
            fuel2.append(i)

print('Fuel Requirements (counting fuel):',sum(fuel1)+sum(fuel2))
