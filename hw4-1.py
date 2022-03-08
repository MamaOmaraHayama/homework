from sys import argv

path, a, b, c = argv
a, b, c = map(int, argv[1:])
wage = (a * b) + c
print(wage)
