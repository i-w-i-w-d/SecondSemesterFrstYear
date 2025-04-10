########## 1 ##########

n = int(input("n = "))
s_n = 0
sign = 1
for i in range(1, n + 1):
    s_n += sign * i
    sign *= -1
print("S_n =", s_n)

########## 2 ##########

n = int(input("n = "))
s_n = 0
for i in range(1, n):
    denominator = i * (i + 1)
    s_n += 1 / denominator
print("S_n =", s_n)

########## 3 ##########

n = int(input("n = "))
s_n = 0
sign = 1
for i in range(2, n + 1):
    s_n += sign * (i - 1) / i
    sign *= -1
print("S_n =", s_n)