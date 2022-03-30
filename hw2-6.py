goods = []
an = {}
name = []
an['название'] = name
cost = []
an['цена'] = cost
number = []
an['количество'] = number
unit = []
an['единицы измерения'] = unit
while input('Хотите добавить товар? - введите да/нет:') == 'да':
    num = int(input('номер товара:'))
    features = {}
    while input('Хотите ввести характеристику продукта? - введите да/нет:') == 'да':
        a = input('введите название продукта:')
        features['название'] = a
        name.append(a)
        b = input('введите цену продукта:')
        features['цена'] = b
        cost.append(b)
        c = input('введите количество продукта:')
        features['количество'] = c
        number.append(c)
        d = input('введите единицы измерения продукта:')
        features['единицы измерения'] = d
        unit.append(c)
        break
    goods.append(tuple([num, features]))
print('товары:', goods)
print('аналитика:', an)







