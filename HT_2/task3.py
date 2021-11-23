#3.Написати скрипт, який видалить пусті елементи із списка.

test_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
res = list(filter(None, test_list))
print ("List after empty list removal : " + str(res))
