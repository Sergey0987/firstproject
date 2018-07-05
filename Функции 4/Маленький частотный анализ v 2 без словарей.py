#спросить про конструкцию, когда идет цикл с ренджем в длинну списка и внутри цикла происходит уменьшение этого списка за счет pop. Как лучше делать с такой конструкцией

def verify_big_letter(stringList):
    global list_of_chars
    
    for i in string:
        if ord(i) >= ord('А') and ord(i) <= ord('Я'):
            list_of_chars.append(chr(ord(i) + distance_between_big_and_small__letters))
        else:
            list_of_chars.append(i)    



def count_of_chars(listChars, listCount):
    global list_of_chars
    global list_of_count
    
    for i in range(len(list_of_chars)):
        counter = 1
        for j in range(i+1, len(list_of_chars)):
            if list_of_chars[i] == list_of_chars[j] and list_of_chars[i] != 'True':
                counter = counter + 1
                list_of_chars[j] = 'True'
        if list_of_chars[i] != 'True':
            list_of_count.append(counter)
        counter = 0

def del_charTrue_from_list(listChars):
    global list_of_chars
    
    i = 0
    while 'True' in list_of_chars:
        if list_of_chars[i] == 'True':
            list_of_chars.pop(i)
        if i+1 > len(list_of_chars)-1: 
            i = 0
        else:
            i = i + 1
   
def maximum_value_definition():
    global maxim
    
    for i in range(len(list_of_count)):
        if i == 0:
            value_maximum = list_of_count[i]
            maxim.append(i)
        else:
            if list_of_count[i] > value_maximum:
                maxim.clear()
                value_maximum = list_of_count[i]
                maxim.append(i)
            elif list_of_count[i] == value_maximum:
                maxim.append(i)    

def print_first_maxim_in_alphabetical_order():
    if len(maxim) == 1:
        value_maxim = list_of_chars[maxim[0]]
    else:
        for i in range(len(maxim)):
            if i == 0:
                value_maxim = ord(list_of_chars[maxim[i]])
                index_char = maxim[i]
            else:
                if ord(list_of_chars[maxim[i]]) < value_maxim:
                    value_maxim = ord(list_of_chars[maxim[i]])
                    index_char = maxim[i]
        value_maxim = chr(value_maxim)
 
    print(value_maxim)


def little_frequency_analysis():
    global string
    global list_of_chars
    global list_of_count
    global counter
    global distance_between_big_and_small__letters  
    global maxim
    string = input()
    list_of_chars = []
    list_of_count = []
    counter = 0
    distance_between_big_and_small__letters = ord('а') - ord('А')    
    maxim = []
    verify_big_letter(string)
    count_of_chars(list_of_chars, list_of_count)
    del_charTrue_from_list(list_of_chars)
    maximum_value_definition()
    print_first_maxim_in_alphabetical_order()






little_frequency_analysis()






















