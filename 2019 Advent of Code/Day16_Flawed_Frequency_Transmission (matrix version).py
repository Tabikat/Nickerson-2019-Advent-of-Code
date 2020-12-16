import os
file=open('Day16.txt').read()

#input=str(3036732577212944063491565474664)
#input_vector=[0,3,0,3,6,7,3,2,5,7,7,2,1,2,9,4,4,0,6,3,4,9,1,5,6,5,4,7,4,6,6,4]
input_vector=[]
for i in file:
    input_vector.append(int(i)) #converts string to list of integers
#input_vector=10000*input_vector

#message_offset=input[:6]
dim=len(input_vector) #dimensions of pattern matrix, height of vector
base_pattern=[0,1,0,-1]

def matrix_construction(row_dimension, pattern):
    RREF_matrix=[[0 for i in range(row_dimension-(row_dimension-i))] for i in range(row_dimension)] #puts all 0's in RREF
    for row in RREF_matrix:
        if RREF_matrix.index(row)>row_dimension:
            while len(row)<row_dimension:
                row.append(base_pattern[1])
        else:
            while len(row)<row_dimension:
                for i in range(RREF_matrix.index(row)+1):
                    row.append(base_pattern[1])
                if len(row)>row_dimension:
                    break
                for i in range(RREF_matrix.index(row)+1):
                    row.append(base_pattern[2])
                if len(row)>row_dimension:
                    break
                for i in range(RREF_matrix.index(row)+1):
                    row.append(base_pattern[3])
                if len(row)>row_dimension:
                    break
                for i in range(RREF_matrix.index(row)+1):
                    row.append(base_pattern[0])
                if len(row)>row_dimension:
                    break
        del row[row_dimension:] #cuts off excess elements
    return RREF_matrix

#print(matrix_construction(dim, base_pattern))

def matrix_multiplication(matrix, input_phase, output_phase):
    for row in matrix: #matrix multiplication
        addends=[]
        element_count=0 #necessary because when checking index, always picks 1st available
        for element in row:
            if row[element_count]!=0:
                addends.append(row[element_count]*input_phase[element_count])
                element_count+=1
            else:
                element_count+=1
                continue
        output_digit=abs(sum(addends))%10
        output_phase.append(output_digit)

def FFT(row_dimension, pattern, vector, num_of_phases):
    phase_count=0
    current_phase=vector
    new_phase=[]
    while phase_count!=num_of_phases:
        matrix_multiplication(matrix_construction(row_dimension, pattern), current_phase, new_phase)
        phase_count+=1
        current_phase=new_phase
        new_phase=[]
        if phase_count==num_of_phases:
            return current_phase[:8]

print(FFT(dim, base_pattern, input_vector, 100))
