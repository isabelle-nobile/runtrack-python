def multiply_between():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

    produit = 1 
    for element in L:
        if 25 <= element <= 90:
            produit *= element
    
    print(produit)

    
multiply_between()