class Matrix:
    def __init__(self, ls):
        self.ls = list(ls)

    def __str__(self):
        for e in self.ls:

            for el in e:
                e = str(e)
                line = ' '.join(e).split()

            newline = [i for i in line if line.index(i) % 2 != 0]
            for n in newline:
                printline = ' | '.join(newline)

            print(printline)

    def __add__(self, other):

        result = [[self.ls[i][j] + other.ls[i][j] for j in range
        (len(self.ls[0]))] for i in range(len(self.ls))]

        for r in result:
            print(r)


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[1, 1, 1], [1, 1, 1]])
a.__str__()
b.__str__()
print(a + b)
