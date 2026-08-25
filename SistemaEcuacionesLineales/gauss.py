A = [
    [1.0, 1.0, 1.0],
    [2.0, 3.0, 1.0],
    [3.0, 2.0, 5.0]
]

b = [6.0, 11.0, 22.0]
n = len(A)
# i indica el aii que estamos usando
for i in range(n - 1):
    #j recorre las filas que estan debajo de aii
    for j in range(i + 1, n):
        factor = A[j][i]/A[i][i]
        #k recorre las columnas de la fila j
        for k in range(i, n):
            A[j][k] = A[j][k] - factor * A[i][k]
            #Tambien modificamos el b
        b[j] = b[j] - factor * b[i]
            
print("Matriz triangukar superior:")
for fila in A:
    print(fila)
print("Vector b modificado:")
print(b)