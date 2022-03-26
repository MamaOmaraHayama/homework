f = open('new.txt', 'a', encoding='utf-8')
while True:
    data = input('Введите данные:')
    f.write(data + "\n")
    if data == '':
        break

f.close()
