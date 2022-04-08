with open('7.txt') as f:
    n = 0
    prof = []
    ls_firm = []
    dict1 = {}
    dict2 = {}
    for line in f:
        ls = line.split()
        a = int(ls[2])
        b = int(ls[3])
        c = a - b
        if c > 0:
            prof.append(c)
        n += 1
        dict1[ls[0]] = c
    s_profit = sum(prof)
    av_profit = s_profit / n
    dict2['average_profit:'] = av_profit
    ls2 = [dict1, dict2]
    print(ls2)

import json
with open('firm.json', 'w', encoding='utf-8') as file:
    json.dump(ls2, file)


