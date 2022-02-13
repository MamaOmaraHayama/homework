# задача 7
a = float(input('начальный результат, км:'))
b = float(input('желаемый результат, км:'))
count = 0
while a <= b:
    a = a * 1.1
    count = count + 1
    print(count)



