#3.Написати скрипт, який видалить пусті елементи із списка.

a = ["Hi", "", 'dear', "", "metor", "", "", "!", (12,24), (), {19:96}, {}, [], '']
while ("" in a):
   a.remove("")
while (() in a):
   a.remove(())
while ({} in a):
    a.remove({})
while ([] in a):
    a.remove([])
while ('' in a):
    a.remove('')

print(a)
