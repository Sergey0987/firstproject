def not_equal_2017():  
    number_2017 = 2017
    count_not_equal_2017 = 0
    count_for = int(input())
    for i in range(count_for):
        number = int(input())
        if number != number_2017:
            count_not_equal_2017 = count_not_equal_2017 + 1
    print(count_not_equal_2017)
    
        
not_equal_2017()


