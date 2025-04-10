'''
xk = 1
x = float(input("x = "))
n = int(input("n = "))
for k in range(1, n + 1):
    xk = - xk * x ** 2 / ((2 * k - 1) * (2 * k))
    print(xk)
'''

'''
S = 1
a = 1
for n in range (2, 11):
    a = -a
    S += a / n

print(S)
'''

'''
Pn = 1
for n in range (1, 11):
    Pn = Pn * (1 + 1 / n ** 2)
    
print(Pn)
'''

a_n = 1
for i in range (1, 5):
    a_n = 1 + 1 / a_n
    print(a_n)