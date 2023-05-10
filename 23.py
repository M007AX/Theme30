def prost(x):
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return 0
    return 1

for n in range(140//2, 200):
    s = n*2+n*1-1
    if prost(s):
        print(n)
        break
