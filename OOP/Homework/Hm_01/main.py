import x1_2_1
from OOP.Homework.Hm_01.x1_2_1 import QuadraticEquation

if __name__ == '__main__':

    def FileRedear(filename):
        equations = []
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip:
                    continue
                coeffs = list(map(float, line.split()))
                while len(coeffs) < 3:
                    coeffs.append(0.0)
                equations.append(QuadraticEquation(*coeffs[:3]))
        return equations

    def analyze(equations):
        NoSolutions = []
        OneSolution = []
        TwoSolutions = []
        InfSolutions = []

        for eq in equations:
            Type = eq.DefineType()
            if Type == 'no':
                NoSolutions.append(eq)
            elif Type == 'one':
                OneSolution.append(eq)
            elif Type == 'two':
                TwoSolutions.append(eq)
            elif Type == 'inf':
                InfSolutions.append(eq)

        for eq in NoSolutions:
            eq.show()

        for eq in OneSolution:
            eq.show()

        for eq in TwoSolutions:
            eq.show()

        for eq in InfSolutions:
            eq.show()

        if OneSolution:
            Min = None
            Max = None
            MinEq = None
            MaxEq = None

            for eq in OneSolution:
                solution = eq.solve()[0]

                if Min is None or solution < Min:
                    Min = solution
                    MinEq = eq

                if Max is None or solution > Max:
                    Max = solution
                    MaxEq = eq

            print('\n')
            MinEq.show()

            print('\n')
            MaxEq.show()

    print('\n')

    equations = FileRedear('input.txt')

    print('\n')

    analyze(equations)