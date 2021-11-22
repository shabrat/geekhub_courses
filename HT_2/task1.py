#1.Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити"

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
    for element in list:
        result += int(element)

print(concatenate_list_data([1, 9, 9, 6, "Hi Mentor"],), 1, 9,9,6)
