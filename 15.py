from itertools import permutations
word = "ССССCГГГ"
A = permutations(word, 6)
counter = 0
for i in A:
    s = "".join(i)
    if s.count("С") > s.count("Г") and s.count("ГГ") == 0:
        counter += 1
print(counter)
