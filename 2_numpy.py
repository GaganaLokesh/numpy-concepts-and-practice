import numpy as np

data=np.array([
    [25, 50000],
    [30, 60000],
    [35, 65000],
    [40, 70000]
    ])   #1stcolumn=age 2nd column=salary
print(data)

print("\nAccessing Features ")
print(data[:,0]) #prints 0 column ":" means → all rows
print(data[:,1]) #prints 1st column | Accessing full column

print("\nExample: Increase salary by 10%")
data[:,1]=data[:,1] *1.1
print("\n After increasing salary=", data[:,1])
print("Average age:", np.mean(data[:,0]))
print("Max salary:", np.max(data[:,1]))

print(data[1,1]) #1st row 1st column
print(data[1]) # Access full row

print("\nPartial slicing= ",data[0:2, 1]) #Rows 0 to 1, column 1:
print("\nFirst 2 rows, both columns= ",data[0:2, 0:2])