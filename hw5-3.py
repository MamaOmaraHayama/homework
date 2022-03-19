f = open('2.txt', 'r', encoding='utf-8')
total_income = 0
st = 0
for i in f:
    ls = i.split()
    e = int(ls[1])
    total_income += e
    st += 1
    if e < 20000:
        print(ls[0])
average_income = total_income / st
print('средний доход: ', average_income)

f.close()
