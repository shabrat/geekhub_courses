#3.Написати скрипт, який видалить пусті елементи із списка.

a = ["Hi", "", "dear", "", "metor", "", "", "!"]
b = []
for string in a:
    if (string != ""):
        b.append(string)
print(b)
