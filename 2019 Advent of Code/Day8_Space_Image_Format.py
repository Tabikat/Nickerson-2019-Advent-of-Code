import os
file=open('Day8.txt').read().strip()
ImageData=list(file)

#breaks the ImageData into chucks of 150
Layers=[] #collection of all layers
zeroes=[] #how many zeroes are in each layer
newlayer=[] #holds each layer until it reaches length 150
for pixel in ImageData:
    if len(newlayer)<150:
        newlayer.append(int(pixel))
    elif len(newlayer)>=150:
        zeroes.append(newlayer.count(0)) #adds the number of 0's to zero list
        Layers.append(newlayer) #adds the layer to the list of layers
        newlayer=[] #clears the holding list to start the new row
        newlayer.append(int(pixel)) #must append this layer here or it will be skipped
Layers.append(newlayer) #must append this layer here or it will be skipped

#finds the layers with the least number of zeroes
print('Part One:',Layers[zeroes.index(min(zeroes))].count(1)*Layers[zeroes.index(min(zeroes))].count(2))

#makes a list of the black and white pixels seen in the final image
picture=[2 for i in range(150)] #makes a list 150 long with all 2's
for layer in Layers:
    p=0 #tracks which pixel we're on within the layer
    for pixel in layer:
        if picture[p]==2: #2 represents transparent pixels
            if pixel==0: #0 represents black
                picture[p]=' '
            elif pixel==1: #1 represents white
                picture[p]='X'
        p+=1

#breaks the picture into chunks of 25, similarly to the first set of instructions
rows=[] #collection of all of the rows of pixels
newrow=[] #holds each row of pixels until it reaches length 25
for pixel in picture:
    if len(newrow)<25:
        newrow.append(pixel)
    elif len(newrow)>=25:
        rows.append(newrow)
        newrow=[]
        newrow.append(pixel) #must append this pixel here or it will be skipped
rows.append(newrow) #must append this row here or it will be skipped

for row in rows: #prints each row individually
    print(row)
