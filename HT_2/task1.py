#1.Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити"

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(["Hi Mentor! ", 1, 9,9,6]))
