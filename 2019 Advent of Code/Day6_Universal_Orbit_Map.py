import os
file=open('Day6.txt').read()
OrbitMap=file.split('\n')
OrbitMap.sort()

OrbitList=[]
for orbit in OrbitMap:
    planet=orbit[0:3]
    moon=orbit[4:7]
    OrbitList.append((planet,moon))

sunlist=[]
planetlist=[]
planetlistunique=[]
moonlist=[]
moononly=[]
moonsperplanet={}
Mercury=[]
Venus=[]
Earth=[]
Mars=[]
Ceres=[]
Jupiter=[]
Saturn=[]
Uranus=[]
Neptune=[]
Pluto=[]
Haumea=[]
Makemake=[]
Eris=[]
for (planet,moon) in OrbitList:
    planetlist.append(planet)
    moonlist.append(moon)
    if planet not in planetlistunique:
        planetlistunique.append(planet)
    if planet not in sunlist:
        sunlist.append(planet)
    if moon not in moononly:
        moononly.append(moon)
for (planet,moon) in OrbitList:
    if moon in sunlist:
        sunlist.remove(moon)
    if planet in moononly:
        moononly.remove(planet)
for (planet, moon) in OrbitList:
    if planet in sunlist:
        Mercury.append(moon)
for (planet, moon) in OrbitList:
    if planet in Mercury:
        Venus.append(moon)
for (planet, moon) in OrbitList:
    if planet in Venus:
        Earth.append(moon)
for (planet, moon) in OrbitList:
    if planet in Earth:
        Mars.append(moon)
for (planet, moon) in OrbitList:
    if planet in Mars:
        Ceres.append(moon)
for (planet, moon) in OrbitList:
    if planet in Ceres:
        Jupiter.append(moon)
for (planet, moon) in OrbitList:
    if planet in Jupiter:
        Saturn.append(moon)
for (planet, moon) in OrbitList:
    if planet in Saturn:
        Uranus.append(moon)
for (planet, moon) in OrbitList:
    if planet in Uranus:
        Neptune.append(moon)
for (planet, moon) in OrbitList:
    if planet in Neptune:
        Pluto.append(moon)
for (planet, moon) in OrbitList:
    if planet in Pluto:
        Haumea.append(moon)
for (planet, moon) in OrbitList:
    if planet in Haumea:
        Makemake.append(moon)
for (planet, moon) in OrbitList:
    if planet in Makemake:
        Eris.append(moon)
#for planet in planetlist:
#    moonsperplanet[planet]=planetlist.count(planet)

print('Sun:',sunlist[0])
print('Mercury:', Mercury)
print('Venus:', Venus)
print('Earth:', Earth)
print('Mars:', Mars)
print('Ceres:', Ceres)
print('Jupiter:', Jupiter)
print('Saturn:', Saturn)
print('Uranus:', Uranus)
print('Neptune:', Neptune)
print('Pluto:', Pluto)
print('Haumea:', Haumea)
print('Makemake:', Makemake)
print('Eris:', Eris)
print('Number of Planets:', len(planetlistunique)-1)
print('Number of Only Moons:', len(moononly))
print('Number of Direct Orbits:',len(OrbitList))


#print(OrbitList)
