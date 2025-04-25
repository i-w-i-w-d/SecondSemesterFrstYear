import math
eps = 0.0000001
x = math.pi / 6
S = a = x
n = 0
#for n in range(1, 15):
while abs(a) >= eps:
    n += 1
    a = -a * x ** 2 / ((2 * n + 1) * 2 * n)
    S += a

print(f'{S           = }')
print(f"{math.sin(x) = }")