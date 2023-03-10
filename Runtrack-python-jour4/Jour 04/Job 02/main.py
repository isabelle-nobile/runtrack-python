def return_list():
    fruits = ['pomme', 'cerise', 'orange']
    cnt=0
    for fruits in fruits:
        cnt+=1
        if cnt==2:
            print(fruits)

return_list()