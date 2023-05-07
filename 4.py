print("z x y w 1 2")
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                print(z, x, y, w, str(((x or not (y)) == (z <= w))).replace("False", "0").replace("True", "1"), str(((not x == (y)) and (z <= w))).replace("False", "0").replace("True", "1"))
