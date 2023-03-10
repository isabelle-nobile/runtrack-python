min = 0
max = 1001

def pracourir_nombres():
    for n in range(min,max + 1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else:
                print(n)

pracourir_nombres()