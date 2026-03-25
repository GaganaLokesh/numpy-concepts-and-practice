import numpy as np

print("\nStep1: Create an Array")
a=np.array([1,2,3,4])  # 1D (vector) #Convert Python list → NumPy array | NumPy array → fast + mathematical | vector + matrix operations in code
print("a= ",a)

print("\nStep 2: Shape")
b=np.array([[1,2,3],[4,5,6]])#2D (matrix)
print("b= ",b)
print("Shape of b:",b.shape)

print("\nStep 3: Indexing")
print("Element at (0,1):",b[0][1]) #2
print(b[1][1]) #5
print("First row:", b[0])
print("Second column:", b[:,1])

print("\nStep 4: Operations")
x=np.array([2,3,4])
y=np.array([1,2,3])

print("\nAddition")
print("x+y= ",x+y)

print("\nMulitiplication ")
print("x*y=" ,x*y)

print("\nMatrix multiplication or .product")
m = np.array([[1,2],[3,4]])
n = np.array([[5,6],[7,8]])
print(np.dot(m, n))

print("\nStep 5: Useful Functions")
print(np.mean(a))
print(np.sum(a))
print(np.max(a))
print(np.min(a))

print("\nStep 6: Reshape")
z=np.array([2,3,4,5,6,7,8,9])
print(z.reshape(2,4))

print("\nSpecial arrays")
print("\n zeros= ",np.zeros((2, 3))) # all 0 
print("\nones= ",np.ones((2, 2))) # all 1 
print("\n arange= ",np.arange(0, 10)) # 0 to 9 
print("\nLinespace= ",np.linspace(0, 1, 5)) # 5 values between 0 and 1 