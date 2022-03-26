
# задача 2

seconds = int(input('time:'))
hours = seconds//3600
seconds = seconds % 3600
minutes = seconds//60
seconds = seconds % 60
print("%02d:%02d:%02d" % (hours, minutes, seconds))

