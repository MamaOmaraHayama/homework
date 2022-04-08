from itertools import count, cycle


for e in count(3):
    if e > 10:
        break
    print(e)

import time
time.sleep(3)

ls = [5, 5, 5, 9, 8, 6, 1]

i = 0
for e in cycle(ls):
    i += 1
    print(e)
    if i > 20:
        break
