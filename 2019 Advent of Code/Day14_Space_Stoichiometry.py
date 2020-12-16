import os
file=open('Day14.txt').read().strip()
nanofactory=file.splitlines()

reactions=[] #list of all of the elements in each reaction
for equation in nanofactory: #each item in nanofactory is one reaction
    elements=equation.split(' ') #splits on spaces
    for part in elements:
        if '=' in part:
            elements.remove(part) #removes the '=>' parts
        elif ',' in part:
            place=elements.index(part)
            piece=part.strip(',')
            elements[place]=piece
    for part in elements:
        if part.isdigit(): #checks if an element is convertable to integer
            place=elements.index(part)
            piece=int(part)
            elements[place]=piece
    elements.insert(0,0) #inserts 0 at index 0
    reactions.append(elements)

chemistrybook={} #keys=products: values=[need counter, reactant quatity, reactant, product quantity]
for elements in reactions:
    chemistrybook[elements[-1]]=elements[:-1] #quantity of product stores in -1
print(chemistrybook)

def atoms(product_in_use):
    for reactant in chemistrybook[product_in_use]:
        if type(reactant)==int:
            continue
        else:
            for product in chemistrybook:
                if reactant in product:
                    chemistrybook[product][0]+=chemistrybook[product_in_use][chemistrybook[product_in_use].index(reactant)-1]
atoms('FUEL')
print(chemistrybook)
