import math

def taylor_series_generator(x, epsilon):
    k = 1
    while True:
        term = 2 * (x ** k) / k
        yield term
        k += 2

def calculate_ln_ratio(x, epsilon=1e-6):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")

    result = 0.0
    series = taylor_series_generator(x, epsilon)

    while True:
        term = next(series)
        result += term
        if abs(term) < epsilon:
            break

    math_result = math.log((1 + x) / (1 - x))

    return result, math_result

x_values = [0.1, 0.2, 0.3, 0.4, 0.5]
epsilon = 1e-6
print("\nЗадача e:")
for x in x_values:
    approx, exact = calculate_ln_ratio(x, epsilon)
    print(f"x = {x}:")
    print(f"  Наближене значення: {approx}")
    print(f"  Точне значення:     {exact}")
    print(f"  Різниця:            {abs(approx - exact)}")