counter = 0
#109568 начало
#154320987 конец
#ответ разность + 1
for i in range(154320986, 154320988):
    for x in range(0, 3):
        n = bin(i)[2::]
        i = str(i)
        even = 0 #чётные
        odd = 0 #нечётные
        for j in range(len(i)):
            if int(i[j]) % 2 == 0:
                even += 1
            else:
                odd += 1
        if even > odd:
            n += "1"
        elif even < odd:
            n += "0"
        else:
            if int(i) % 2 == 0:
                n += "0"
            else:
                n += "1"
        i = int(n, 2)
    R = int(n, 2)
    if 876544 <= R <= 1234567899:
        counter += 1
print(counter)
#or
print(154320987 - 109568 + 1)
