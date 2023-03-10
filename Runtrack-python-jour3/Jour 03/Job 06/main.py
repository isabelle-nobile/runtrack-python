def parcourir_nombres():
    row = 10
    string = "abcdefghijklmnopqrstuvwxyz"

    for i in range(row):
        tmp = string[:i+1]
        print(tmp[::-1])


parcourir_nombres()
