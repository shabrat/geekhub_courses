Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку

start = int (input ("Enter start year: "))
end = int (input ("Enter end year: "))
if start >= end or start == 0:
    print ("Неверный диапазон!")
    exit ()

for year in range (start, end + 1):
    if year % 4 == 0:
        print (year)
        year += 1
