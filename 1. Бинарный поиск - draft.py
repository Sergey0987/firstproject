list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
index_min=0 #самый левый индекс в интервале
index_max=len(list1)-1 #самый правый индекс в интерале
search_number=int(input('Введи число от '+str(list1[0])+' до '+str(list1[len(list1)-1])+': '))

while search_number not in list1: # проверка корректности ввода искомого числа
    print('Вы ввели число за пределами интервала!')
    search_number=int(input('Введи число от '+str(list1[0])+' до '+str(list1[len(list1)-1])+': '))
    print(search_number)


while search_number != list1[index_max] and search_number != list1[index_min]:
    if search_number < list1[index_max//2]:
        index_max=(index_max//2)
        print('index_max',index_max)
    elif search_number > list1[index_max//2]:
        if search_number < list1[index_min+(index_max-index_min)//2]:
            index_max=index_min+(index_max-index_min)//2
            print('index_max',index_max)
        elif search_number > list1[index_min+(index_max-index_min)//2]:
            index_min=index_min+(index_max-index_min)//2
            print('index_min',index_min)
        else:
            index_min=index_min+(index_max-index_min)//2
    elif search_number == list1[index_max//2]:
        index_max=index_max//2

if search_number == list1[index_max]:
    print('Индекс искомого значения ', list1[index_max], ' = ',index_max)
else:
    print('Индекс искомого значения', list1[index_min], ' = ', index_min)
    
    

