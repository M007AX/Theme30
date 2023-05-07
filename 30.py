for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        if not (((x & 116 != 0) or (x & 92 != 0)) <= ((x & 69 == 0) <= (x & A != 0))):
            flag = False
    if flag:
        print(A)
