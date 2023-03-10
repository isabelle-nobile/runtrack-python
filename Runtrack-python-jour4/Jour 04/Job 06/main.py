def return_list():
    list =[1, 2, 3, 4, 5]
    temp = list[0]
    list[0]=list[-1]
    list[-1]=temp
    return list

return_list()