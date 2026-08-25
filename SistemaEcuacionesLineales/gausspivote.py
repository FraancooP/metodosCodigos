A = [
    [0.0, 2.0, 1.0],
    [2.0, 1.0, -1.0],
    [0.0, 1.0, 2.0]
]

b = [7.0, 1.0, 8.0]
n = len(A)



#Gauss con pivoteo parcial y eliminacion=========================================
for i in range(n - 1):
    fila_pivote = i
    for fila in range(i + 1, n):
        if abs(A[fila][i]) > abs(A[fila_pivote][i]):
            fila_pivote = fila
    
    
    if abs(A[fila_pivote][i]) < 1e-12:
        print("La matriz puede ser singular o casi singular.")
        break
    
    if fila_pivote != i:
        A[i], A[fila_pivote] = A[fila_pivote], A[i]
        b[i], b[fila_pivote] = b[fila_pivote], b[i]
        
    for j in range(i + 1, n):
        factor = A[j][i] / A[i][i]
        for k in range(i, n):
            A[j][k] = A[j][k] - factor * A[i][k]
        b[j] = b[j] - factor * b[i]
#==============================================================================
            
print("Matriz triangular superior:")
for fila in A:
    print(fila)
print("Vector b modificado:")
print(b)

x = [0.0] * n
for i in range(n - 1, -1, -1):
    suma = 0.0
    for j in range(i + 1, n):
        suma = suma + A[i][j] * x[j]
    x[i] = (b[i] - suma) / A[i][i]
    
print("Vector solucion:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")