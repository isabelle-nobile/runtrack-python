def draw_rectangle(heigth, width):
    for i in range(width):
        for j in range(heigth):
            if j ==0 or j ==(heigth -1):
                print("|", end="") 
            elif i ==0 or i == (width -1):
                print("-", end="")
            else:
                print(" ", end="")
        print()

draw_rectangle(10,3)
