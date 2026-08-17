A = []


B = []

print("Enter values for Matrix A(3,3)")
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"A[{i}][{j}] = "))
        row.append(value)
    A.append(row)

print("Enter values for Matrix B(3,3)")
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"B[{i}][{j}] = "))
        row.append(value)
    B.append(row)
    
result = [[0 for _ in range(3)] for _ in range(3)]
        
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix A = ")
for row in A:
    print(row)
    
print("Matrix B = ")
for row in B:
    print(row)
    
print("Product Matrix(A * B) = ")
for row in result:
    print(row)