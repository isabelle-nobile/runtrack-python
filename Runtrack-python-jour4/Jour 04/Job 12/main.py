def tri_liste(liste):
    n = 0
    while True:
        try:
            _ = liste[n]
            n += 1
        except IndexError:
            break
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste


liste = [15, 8, 45, 13]
print(tri_liste(liste))
