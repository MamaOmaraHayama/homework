# задача 5-6
r = int(input('выручка:'))
ls = int(input('издержки:'))
p = r/ls
if p >= 1:
    print('прибыль')
    rent = (r - ls)/r
    print('рентабельность:', rent)
    n = int(input('численность сотрудников:'))
    m = (r - ls)/n
    print('прибыль на одного сотрудника:', m)
else:
    print('убыток')

