tab = [12, 6, 4, 9, 3]
for x in tab:
    kolumna = str()
    i = 0
    while i != x:
        kolumna += '*'
        i += 1
    print(f"{x}: {kolumna}")