alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for p in range(2, 37):
    for x in alphabet:
        for y in alphabet:
            for z in alphabet:
                first = y + "4" + y
                second = y + "65"
                ans = x + z + "23"
                try:
                    if int(first, p) + int(second, p) == int(ans, p):
                        print(int(x + y + z, p))
                except:
                    continue
