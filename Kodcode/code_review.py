list_1 = []
list_2 = []
list_3 = []

for num in range(3):
    list_1.append(num)

print(list_1)



last = list_1[-1] // 2
length = len(list_1) * 2

data = {"last": last, "length": length}

for i in range(data["length"]):
    if i < len(list_1):
        item = list_1[i]
        list_2.append((item - 1) ** 2)
    else: #[3,4,5]
        list_2.append(1 - (i % 2))

print(list_2)


while len(list_2) > 0:
    x = list_2.pop() + list_2.pop()
    list_3.append(x)

print(list_3)


is_in_list = data['last'] in list_3
print(is_in_list)
print(is_in_list and bool(len(list_2)))


