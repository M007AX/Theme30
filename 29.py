for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        if not (((x & 114 != 0) or (x & 94 != 0)) <= ((x & 73 == 0) <= (x & A != 0))):
            flag = False
    if flag:
        print(A)
