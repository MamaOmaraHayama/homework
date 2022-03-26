f = open('3.txt', 'r', encoding='utf-8')

new = ['один', 'два', 'три', 'четыре']
n = 0
for i in f:
    file = open('4.txt', 'a', encoding='utf-8')
    ls = i.split()
    ls[0] = new[n]
    n = n + 1
    st = ' '.join(ls)
    file.write(st + "\n")
    file.close()

f.close()
