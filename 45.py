alphabet = " 0123456789"
for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            for q in "0123456789":
                word = "1" + q + "3948" + x1 + x2 + x3 + "5"
                word = word.replace(" ", "")
                if int(word) % 3013 == 0 and int(word) <= 10**10:
                    print(word)
