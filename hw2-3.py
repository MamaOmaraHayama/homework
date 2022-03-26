season = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
num = int(input('1-12:'))
for el in season:
    if num in season[el]:
        print(el)

saeson = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
spring = [3, 4, 5]
autumn = [9, 10, 11]
summer = [6, 7, 8]
winter = [1, 2, 12]
num = int(input('1-12:'))
for e in season:
    if num in spring:
        print('spring')
        break
    if num in autumn:
        print('autumn')
        break
    if num in summer:
        print('summer')
        break
    if num in winter:
        print('winter')
        break
else:
    print('none')


