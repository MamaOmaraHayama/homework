ls = input('введите числа:').split()
print('before:', ls)
n = len(ls)
m = 0
for e in ls:
    ls[m], ls[m+1] = ls[m+1], ls[m]
    m = m + 2
    if m + 2 > n:
        break
print('after:', ls)
