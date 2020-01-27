import numpy as np

test_matrix = np.arange(25).reshape(5,5)

print('Input Numpy Array:')
print(test_matrix)

# Consider first row/column zero
i = int(input("Enter element row number: "))
j = int(input("Enter element column number: "))

# Consider only odd number of order
order = int(input("Enter order of matrix: "))

matnxn = []   # create a blank nxn matrix of surrounding elemnts as a list 

for x in range(-int(order/2),int(order/2)+1): # for each row of nxn matrix
    for y in range(-int(order/2),int(order/2)+1): # for each colimn of nxn matrix
        try:
            if j+y<0 or i+x<0:
                matnxn.append(0)
            else:
                matnxn.append(test_matrix[i+x,j+y])
        except IndexError:
            matnxn.append(0)

output = np.array(matnxn).reshape(order,order)
print('Output Numpy Array:')
print(output)
