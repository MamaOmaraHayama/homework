f = open('5.txt', 'w', encoding='utf-8')
print('23 56 876 32 5 8', file=f)
f.close()

f = open('5.txt', 'r', encoding='utf-8')
su = 0
for i in f:
    ls = i.split()
    for e in ls:
        e = int(e)
        su += e
    print(su)

f.close()
