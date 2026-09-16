import math

x_datos = [0.0, 3.0, 6.0]
y_datos = [1.0, 2.0, 8.0]

x_evaluar = 4

sum = 0.0

n = len(x_datos)

for k in range(n):
    producto = 1.0
    for i in range(n):
        if i != k:
            producto *= (x_evaluar - x_datos[i]) / (x_datos[k] - x_datos[i])
    sum += producto * y_datos[k]
    

print("Valor interpolado:", sum)
