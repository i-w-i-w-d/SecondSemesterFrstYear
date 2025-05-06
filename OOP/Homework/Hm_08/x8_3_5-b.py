def P_n_generator(n):
    product = 1.0
    for i in range(1, n + 1):
        product *= (1 + 1 / (i * i))
        yield product

def calculate_P_n(n):
    if n < 1:
        raise ValueError("n має бути додатним")

    product = 1.0
    for i in range(1, n + 1):
        product *= (1 + 1 / (i * i))
    return product

n_values = [1, 2, 3, 4, 5]
print("\nЗадача b:")
for n in n_values:
    print(f"P_{n} = {calculate_P_n(n)}")