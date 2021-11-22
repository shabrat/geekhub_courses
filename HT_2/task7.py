#7.Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.

dict = {'a':1, 'b':-1, 'c': 1996, 'd': 5, 'e': 12}

key_max = max(dict.keys(), key=(lambda k: dict[k]))
key_min = min(dict.keys(), key=(lambda k: dict[k]))

print('Minimum Value: ',dict[key_min])
print('Maximum Value: ',dict[key_max])
