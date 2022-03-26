old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for el in old if el > old[old.index(el) - 1]]
print(new)
