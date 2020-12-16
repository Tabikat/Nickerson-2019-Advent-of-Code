import os
file=open('Day11.txt').read()
moonspos=file.split('\n')

Io=moonspos[0]
Io=Io[1:-1]
Europa=moonspos[1]
Europa=Europa[1:-1]
Ganymede=moonspos[2]
Ganymede=Ganymede[1:-1]
Callisto=moonspos[3]
Callisto=Callisto[1:-1]

#moons={'Io':(-1,0,2),'Europa':(2,-10,-7),'Ganymede':(4,-8,8),'Callisto':(3,5,-1)}
IoPos=[-19,-4,2] #Io
IoVel=[0,0,0]
EuPos=[-9,8,-16] #Europa
EuVel=[0,0,0]
GaPos=[-4,5,-11] #Ganymede
GaVel=[0,0,0]
CaPos=[1,9,-13] #Callisto
CaVel=[0,0,0]

def velocity(moon1,moon2,moon3,moon4,moon1vel):
    if moon1[0]<moon2[0]: #compares x-coordinates
        moon1vel[0]+=1
    if moon1[0]<moon3[0]:
        moon1vel[0]+=1
    if moon1[0]<moon4[0]:
        moon1vel[0]+=1
    if moon1[0]>moon2[0]:
        moon1vel[0]-=1
    if moon1[0]>moon3[0]:
        moon1vel[0]-=1
    if moon1[0]>moon4[0]:
        moon1vel[0]-=1
    if moon1[1]<moon2[1]: #compares y-coordinates
        moon1vel[1]+=1
    if moon1[1]<moon3[1]:
        moon1vel[1]+=1
    if moon1[1]<moon4[1]:
        moon1vel[1]+=1
    if moon1[1]>moon2[1]:
        moon1vel[1]-=1
    if moon1[1]>moon3[1]:
        moon1vel[1]-=1
    if moon1[1]>moon4[1]:
        moon1vel[1]-=1
    if moon1[2]<moon2[2]: #compares z-coordinates
        moon1vel[2]+=1
    if moon1[2]<moon3[2]:
        moon1vel[2]+=1
    if moon1[2]<moon4[2]:
        moon1vel[2]+=1
    if moon1[2]>moon2[2]:
        moon1vel[2]-=1
    if moon1[2]>moon3[2]:
        moon1vel[2]-=1
    if moon1[2]>moon4[2]:
        moon1vel[2]-=1

def position(moonpos,moonvel): #applies velocities to positions
    moonpos[0]+=moonvel[0]
    moonpos[1]+=moonvel[1]
    moonpos[2]+=moonvel[2]

for i in range(1000):
    velocity(IoPos,EuPos,GaPos,CaPos,IoVel)
    velocity(EuPos,IoPos,GaPos,CaPos,EuVel)
    velocity(GaPos,EuPos,IoPos,CaPos,GaVel)
    velocity(CaPos,EuPos,GaPos,IoPos,CaVel)
    position(IoPos,IoVel)
    position(EuPos,EuVel)
    position(GaPos,GaVel)
    position(CaPos,CaVel)

IoEnergy=0
EuEnergy=0
GaEnergy=0
CaEnergy=0
def energy(moonpos,moonvel,moonenergy):
    potential=abs(moonpos[0])+abs(moonpos[1])+abs(moonpos[2])
    kinetic=abs(moonvel[0])+abs(moonvel[1])+abs(moonvel[2])
    moonenergy=potential*kinetic
    return moonenergy

IoEnergy=energy(IoPos,IoVel,IoEnergy)
EuEnergy=energy(EuPos,EuVel,EuEnergy)
GaEnergy=energy(GaPos,GaVel,GaEnergy)
CaEnergy=energy(CaPos,CaVel,CaEnergy)
system=IoEnergy+EuEnergy+GaEnergy+CaEnergy
print('Total Energy for All Moons:',system)
