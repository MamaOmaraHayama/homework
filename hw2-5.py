ls = [8, 7, 6, 4, 2]
a = int(input('введите значение:'))
for e in range(0, len(ls)):
    if a == ls[e]:
        ls.insert(e + 1, a)
        print(ls)
        break
    elif a > ls[0]:
        ls.insert(0, a)
        print(ls)
    elif a < ls[- 1]:
        ls.append(a)
        print(ls)
    elif ls[e] > a > ls[e + 1]:
        ls.insert(e + 1, a)
        print(ls)
        break




