print("x z y w")
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                print(x, z, y, w, ((x <= y) == (w or not (z))), ((x <= y) and (not(w) == z)))
