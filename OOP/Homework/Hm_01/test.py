import math


class QuadraticEquation:
    """
    Клас для представлення квадратного рівняння виду ax² + bx + c = 0.

    Атрибути:
        a (float): коефіцієнт при x²
        b (float): коефіцієнт при x
        c (float): вільний член

    Методи:
        __init__: ініціалізує об'єкт квадратного рівняння
        __copy__: конструктор копіювання
        solve: повертає розв'язки рівняння
        show: виводить рівняння у зручному форматі
        solution_type: повертає тип розв'язків (без розв'язків, один, два чи нескінченність)
    """

    def __init__(self, a, b, c):
        """Ініціалізує квадратне рівняння з коефіцієнтами a, b, c."""
        self.a = a
        self.b = b
        self.c = c

    def __copy__(self):
        """Конструктор копіювання для квадратного рівняння."""
        return QuadraticEquation(self.a, self.b, self.c)

    def solve(self):
        """
        Повертає розв'язки квадратного рівняння.

        Повертає:
            list: список розв'язків (може бути порожнім, з одним або двома розв'язками)
            str: "infinite" якщо рівняння має нескінченну кількість розв'язків
        """
        # Випадок лінійного рівняння (a = 0)
        if self.a == 0:
            # Випадок 0x + 0 = 0 - нескінченність розв'язків
            if self.b == 0 and self.c == 0:
                return "infinite"
            # Випадок 0x + c = 0, c ≠ 0 - немає розв'язків
            if self.b == 0 and self.c != 0:
                return []
            # Лінійне рівняння bx + c = 0 - один розв'язок
            return [-self.c / self.b]

        # Обчислення дискримінанта
        discriminant = self.b ** 2 - 4 * self.a * self.c

        # Різні випадки на основі дискримінанта
        if discriminant < 0:
            return []
        elif discriminant == 0:
            return [-self.b / (2 * self.a)]
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            x1 = (-self.b - sqrt_discriminant) / (2 * self.a)
            x2 = (-self.b + sqrt_discriminant) / (2 * self.a)
            return [x1, x2]

    def show(self):
        """Виводить рівняння у зручному для читання форматі."""
        print(f"{self.a}x2 + {self.b}x + {self.c}")

    def solution_type(self):
        """
        Повертає тип розв'язків рівняння.

        Повертає:
            str: "no" - немає розв'язків
                 "one" - один розв'язок
                 "two" - два розв'язки
                 "infinite" - нескінченна кількість розв'язків
        """
        solutions = self.solve()
        if solutions == "infinite":
            return "infinite"
        return ["no", "one", "two"][min(len(solutions), 2)]


def read_equations_from_file(filename):
    """
    Читає квадратні рівняння з файлу.

    Аргументи:
        filename (str): ім'я файлу з коефіцієнтами

    Повертає:
        list: список об'єктів QuadraticEquation
    """
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            # Пропускаємо порожні рядки
            if not line.strip():
                continue
            # Розбиваємо рядок на коефіцієнти
            coeffs = list(map(float, line.split()))
            # Додаємо нульові коефіцієнти, якщо їх не вистачає
            while len(coeffs) < 3:
                coeffs.append(0.0)
            equations.append(QuadraticEquation(*coeffs[:3]))
    return equations


def analyze_equations(equations):
    """
    Аналізує список квадратних рівнянь та виводить результати.

    Аргументи:
        equations (list): список об'єктів QuadraticEquation
    """
    # Категорії рівнянь
    no_solution = []
    one_solution = []
    two_solutions = []
    infinite_solutions = []

    # Розподіляємо рівняння по категоріям
    for eq in equations:
        sol_type = eq.solution_type()
        if sol_type == "no":
            no_solution.append(eq)
        elif sol_type == "one":
            one_solution.append(eq)
        elif sol_type == "two":
            two_solutions.append(eq)
        elif sol_type == "infinite":
            infinite_solutions.append(eq)

    # Виводимо результати
    print("Рівняння без розв'язків:")
    for eq in no_solution:
        eq.show()

    print("\nРівняння з одним розв'язком:")
    for eq in one_solution:
        eq.show()

    print("\nРівняння з двома розв'язками:")
    for eq in two_solutions:
        eq.show()

    print("\nРівняння з нескінченною кількістю розв'язків:")
    for eq in infinite_solutions:
        eq.show()

    # Знаходимо рівняння з найменшим та найбільшим розв'язком (серед рівнянь з одним розв'язком)
    if one_solution:
        min_solution = None
        max_solution = None
        min_eq = None
        max_eq = None

        for eq in one_solution:
            solution = eq.solve()[0]
            if min_solution is None or solution < min_solution:
                min_solution = solution
                min_eq = eq
            if max_solution is None or solution > max_solution:
                max_solution = solution
                max_eq = eq

        print("\nРівняння з одним розв'язком, що має найменший розв'язок:")
        min_eq.show()
        print(f"Розв'язок: {min_solution}")

        print("\nРівняння з одним розв'язком, що має найбільший розв'язок:")
        max_eq.show()
        print(f"Розв'язок: {max_solution}")


# Основна частина програми
if __name__ == "__main__":
    # Читаємо рівняння з файлу
    equations = read_equations_from_file("input.txt")

    # Аналізуємо рівняння
    analyze_equations(equations)