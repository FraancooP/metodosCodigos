import math

x = [0.2, 0.6, 1.3, 1.4, 1.8, 2.0]
y = [-0.94, -0.26, 2.35, 2.94, 5.45, 7.20]
    


# Funciones que acompañan a a, b y c
#f(x) = a*sen(x) + b*exp(x) + c*log(x)
f1 = [math.sin(xi) for xi in x]
f2 = [math.exp(xi) for xi in x]
f3 = [math.log(xi) for xi in x]

# Matriz A
A = [
    [sum(v*v for v in f1),
     sum(f1[i]*f2[i] for i in range(len(x))),
     sum(f1[i]*f3[i] for i in range(len(x)))],

    [sum(f2[i]*f1[i] for i in range(len(x))),
     sum(v*v for v in f2),
     sum(f2[i]*f3[i] for i in range(len(x)))],

    [sum(f3[i]*f1[i] for i in range(len(x))),
     sum(f3[i]*f2[i] for i in range(len(x))),
     sum(v*v for v in f3)]
]

# Vector b
b = [
    sum(y[i]*f1[i] for i in range(len(x))),
    sum(y[i]*f2[i] for i in range(len(x))),
    sum(y[i]*f3[i] for i in range(len(x)))
]

print("A:")
for fila in A:
    print(fila)

print("b =", b)