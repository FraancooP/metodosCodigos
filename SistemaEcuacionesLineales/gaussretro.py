A = [
    [2.0, 3.0, 1.0],
    [0.0, 4.0, 2.0],
    [0.0, 0.0, 5.0]
]

b = [10.0, 8.0, 15.0]
n = len(A)

#Aca simplemente hacemos eliminacion por gauss==================================
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