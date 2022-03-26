f = open('1.txt', 'r', encoding='utf-8')
st = 0
for i in f:
    st += 1
    wrd = len(i.split())
    print('количество слов в строке:', wrd)
print('количество строк:', st)

f.close()
