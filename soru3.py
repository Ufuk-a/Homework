def square_sorter(list):
    for index, i in enumerate(list):
        list[index] = i * i

    list.sort()
    print(list)    

numbers = [2, 14, 9, 46, 20]        
square_sorter(numbers)    
