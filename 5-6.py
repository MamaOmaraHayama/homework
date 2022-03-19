f = open('6.txt', 'r', encoding='utf-8')
d = {}

for i in f:
    n = []
    ls = i.split()
    ls1 = ls[1].split('(')
    try:
        ls1[0] = int(ls1[0])
        n.append(ls1[0])
    except ValueError:
        continue
    finally:
        ls2 = ls[2].split('(')
        try:
            ls2[0] = int(ls2[0])
            n.append(ls2[0])
        except ValueError:
            continue
        finally:
            ls3 = ls[3].split('(')
            try:
                ls3[0] = int(ls3[0])
                n.append(ls3[0])
            except ValueError:
                continue
            finally:
                d[ls[0]] = sum(n)

print(d)

f.close()


