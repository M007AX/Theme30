def F(a, turn):
    if a > 24:
        return 0
    if a == 24:
        return 1
    else:
        if turn == 0:
            return F(a + 1, 1) + F(a + 2, 1)
        else:
            return F(a * 2, 0) + F(a * 3, 0)
print(F(1, 0) + F(1, 1))
