old = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [e for e in old if old.count(e) == 1]

print(new)
