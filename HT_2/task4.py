dic1={1:11, 2:22}
dic2={3:33, 4:44}
dic3={5:55,6:66}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
