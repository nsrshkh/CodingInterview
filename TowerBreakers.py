def towerBreakers(n, m):
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1


n = 1
m = 4

print(towerBreakers(n, m))
