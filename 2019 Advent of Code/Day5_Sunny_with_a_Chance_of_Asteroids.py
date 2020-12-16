import os
print(os.getcwd())
file=open('Day5.txt').read()
IntcodeInitial=file.split(',')

for i in range(0,len(IntcodeInitial)):
    IntcodeInitial[i]=int(IntcodeInitial[i])

#def memory(noun, verb):
Intcode=list(IntcodeInitial)
i=0
#Intcode[1]=noun
#Intcode[2]=verb
while i<=len(Intcode):
    if Intcode[i]==1:
        addend1=Intcode[i+1]
        addend2=Intcode[i+2]
        Sum=Intcode[addend1]+Intcode[addend2]
        position=Intcode[i+3]
        Intcode[position]=Sum
        i+=4
    elif Intcode[i]==2:
        factor1=Intcode[i+1]
        factor2=Intcode[i+2]
        Product=Intcode[factor1]*Intcode[factor2]
        position=Intcode[i+3]
        Intcode[position]=Product
        i+=4
    elif Intcode[i]==3:
        position=Intcode[i+1]
        Intcode[position]=input
        i+=2
    elif Intcode[i]==4:
        position=Intcode[i+1]
        print(Intcode[position])
        i+=2
    elif Intcode[i]==99:
        break

#return Intcode[0]
#print(memory(12,2))

#for noun in range(100):
#    for verb in range(100):
#        if memory(noun,verb)==19690720:
#            print('Address 0:',memory(noun,verb))
#            print('Noun:',noun)
#            print('Verb:',verb)
#        else:
#            continue
