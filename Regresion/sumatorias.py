x = [0.2, 0.6, 1.3, 1.4, 1.8, 2.0]
y = [-0.94, -0.26, 2.35, 2.94, 5.45, 7.20]

#ax**2 + bx + c
sx = sum(x)
sx2 = sum(xi**2 for xi in x)
sx3 = sum(xi**3 for xi in x)
sx4 = sum(xi**4 for xi in x)

sy = sum(y)
sxy = sum(x[i]*y[i] for i in range(len(x)))
sx2y = sum((x[i]**2)*y[i] for i in range(len(x)))

print("Σx =", sx)
print("Σx² =", sx2)
print("Σx³ =", sx3)
print("Σx⁴ =", sx4)
print("Σy =", sy)
print("Σxy =", sxy)
print("Σx²y =", sx2y)