#6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна "захардкодити".

a = {'a': 1, 'b': 2}
b = {'c': 10, 'd': 11}
c = {'e': 10, 'f': 11}
a.update(b)
a.update(c)
print(a)
