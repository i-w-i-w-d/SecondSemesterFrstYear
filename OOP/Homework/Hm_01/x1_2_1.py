import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __copy__(self):
        return QuadraticEquation(self.a, self.b, self.c)

    def solve(self):
        if self.a == 0:

            if self.b == 0 and self.c == 0:
                return ['infinite']

            if self.b == 0 and self.c != 0:
                return []

            return [-self.c / self.b]

        discriminant = self.b ** 2 - 4 * self.a * self.c

        if discriminant < 0:
            return []

        elif discriminant == 0:
            return [-self.b / (2 * self.a)]

        else:
            x1 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            return [x1, x2]

    def show(self):
        print(f'{self.a}x^2 + {self.b}x + {self.c}')

    def DefineType(self):
        solution = self.solve()
        if solution == 'infinite':
            return ['inf']
        return ['no', 'one', 'two'][min(len(solution), 2)]