from itertools import permutations
word = "ССССГГГ"
A = permutations(word, 5)
counter = 0
for i in A:
    s = "".join(i)
    if s.count("С") > s.count("Г") and s.count("ГГ") == 0:
        counter += 1
print(counter)
