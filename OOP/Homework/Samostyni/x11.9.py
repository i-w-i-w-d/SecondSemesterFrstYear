########## 1 ##########

n = int(input("n = "))
p_n = 1
for i in range(2, n + 1):
    term = 1 - 1 / (i * i)
    p_n *= term
print("P_n =", p_n)

########## 2 ##########

n = int(input("n = "))
p_n = 1
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    term = 2 + 1 / factorial
    p_n *= term
print("P_n =", p_n)

########## 3 ##########

n = int(input("n = "))
p_n = 1
for i in range(1, n + 1):
    term = (i + 1) / (i + 2)
    p_n *= term
print("P_n =", p_n)