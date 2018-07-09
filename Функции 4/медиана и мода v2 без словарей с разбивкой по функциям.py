#МОДА - наиболее часто встречающееся число ряда
#МЕДИАНА - это середина ряда

#самый простой способ был бы сделать превратить список во множество (для составления списка уникальных значений), а затем через функцию count посчитать количество каждого элемента. И поочередно сравнивать. Я же буду делать длинным путем.


def modaAndMediana():
    global list_of_numbers
    global list_of_count
    global index
    list_of_numbers = input().split()
    list_of_count = []
    index = 0
    from_str_to_list(list_of_numbers)
    mediana(list_of_numbers)
    count_frequency_of_numbers()
    del_unnecessary()
    find_moda()
    

def from_str_to_list(listStr):  
    global list_of_numbers
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = int(list_of_numbers[i])
    print(list_of_numbers)    


def mediana(listNum):
    mediana = list_of_numbers[len(list_of_numbers)//2]
    print(mediana)    


def count_frequency_of_numbers():
    global list_of_numbers
    global list_of_count
    for i in range(len(list_of_numbers)-1):
        if list_of_numbers[i] != 'DEL':
            list_of_count.append(1)        
            for j in range(i+1,len(list_of_numbers)): 
                print(i,j)
                if list_of_numbers[i] == list_of_numbers[j]:
                    list_of_count[len(list_of_count)-1] = list_of_count[len(list_of_count)-1] + 1
                    list_of_numbers[j] = 'DEL'

    print(list_of_numbers, list_of_count)    



def del_unnecessary():
    global list_of_numbers
    index = 0
    while 'DEL' in list_of_numbers:
        if list_of_numbers[index] == 'DEL':
            list_of_numbers.pop(index)
        if index + 1 > len(list_of_numbers)-1:
            index = 0
        else:
            index = index + 1

    print(list_of_numbers)    
    


def find_moda():
    global index
    maxim_count = list_of_count[0]
    index = 0
    for i in range(1, len(list_of_count)):
        if maxim_count < list_of_count[i]:
            maxim_count = list_of_count[i]
            index = i

    moda = list_of_numbers[index]

    print('index = ', index, 'moda = ', moda)    
            
        
modaAndMediana()
