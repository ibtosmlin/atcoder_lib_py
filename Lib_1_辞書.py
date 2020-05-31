dic = {}
dic = {str(i):i for i in range(10)}

dic = {'key1': 1, 'key2': 2, 'key3': 3}
for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

for k, v in dic.items():
    print(k, v)


dics = sorted(dic.items(), key=lambda x: x[0])
dics = sorted(dic.items(), key=lambda x: x[1])