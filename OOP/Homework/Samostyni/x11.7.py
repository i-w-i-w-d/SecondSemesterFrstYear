########## 1 ##########

x = float(input("x = "))
k = int(input("k = "))
numerator = 1
for i in range(1, 2 * k + 2):
    numerator *= x
denominator = 1
for i in range(1, 2 * k + 2):
    denominator *= i
xk = numerator / denominator
print("x_k =", xk)

########## 2 ##########

x = float(input("x = "))
k = int(input("k = "))
sign = -1 if k % 2 else 1
xk_power = 1
for i in range(1, k + 1):
    xk_power *= x
xk = sign * xk_power / k
print("x_k =", xk)

########## 3 ##########

x = float(input("x = "))
k = int(input("k = "))
sign = -1 if k % 2 else 1
xk_power = 1
for i in range(1, k + 1):
    xk_power *= x
factorial = 1
for i in range(1, k * k + k + 1):
    factorial *= i
xk = sign * xk_power / factorial
print("x_k =", xk)

########## 4 ##########

x = float(input("x = "))
k = int(input("k = "))
xk_power = 1
for i in range(1, k + 1):
    xk_power *= x
factorial = 1
for i in range(1, k + 1):
    factorial *= i
xk = (k + 1) * xk_power / factorial
print("x_k =", xk)