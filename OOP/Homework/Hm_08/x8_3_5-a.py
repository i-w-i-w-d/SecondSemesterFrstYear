def x_k_generator(x, max_k):
    term = 1
    yield term

    for k in range(1, max_k + 1):
        term *= x * x / ((2 * k) * (2 * k - 1))
        yield term

def calculate_x_k(x, k):
    if k < 0:
        raise ValueError("k має бути невід'ємним")

    result = 1.0
    for i in range(1, k + 1):
        result *= x * x / ((2 * i) * (2 * i - 1))
    return result

x = 2
k_values = [0, 1, 2, 3, 4]
print("Задача a:")
print("x =", x)
for k in k_values:
    print(f"x_{k} = {calculate_x_k(x, k)}")