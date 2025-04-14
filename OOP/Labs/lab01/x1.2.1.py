class QuadraticEquation:
    def __init__(self, a, b, c):
        if isinstance(a, QuadraticEquation):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c
            if not self.isExist():
                raise ValueError("Ділення на 0")

    def isExist(self):
        return isinstance(self.a, (int, float)) and self.a != 0

    def d(self):
        return self.b ** 2 - (4 * self.a * self.c)

    def solve(self):
        if self.d() > 0:
            x1 = (-self.b - (self.d() ** 0.5)) / (2 * self.a)
            x2 = (-self.b + (self.d() ** 0.5)) / (2 * self.a)
            return (x1, x2)

        elif self.d() == 0:
            x = -self.b / (2 * self.a)
            return (x,)

        else:
            return ()

    def show(self):
        roots = self.solve()
        if len(roots) == 1:
            return f"x = {roots[0]}"
        elif len(roots) == 2:
            return f"x1 = {roots[0]}, x2 = {roots[1]}"

def files(input, output):
     with open(input, "r") as infile, open(output, "w") as outfile:
         for line in infile:
             try:
                 a, b, c = map(float, line.strip().split())
                 eq = QuadraticEquation(a, b, c)
                 result = eq.show()
                 outfile.write(f"Рівняння: {a}x^2 + {b}x + {c}\n")
                 outfile.write(f"Результати: {result}\n\n")
             except ValueError as x:
                 outfile.write(f"Дійсних коренів немає\n\n")

if __name__ == "__main__":
    files('input01.txt', 'output.txt')