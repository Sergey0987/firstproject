def modaAndMediana():
    number_string = input().split()
    for i in range(len(number_string)):
        number_string[i] = int(number_string[i])

    if len(number_string)%2 != 0:
        mediana = number_string[int(len(number_string)/2)-1]
    else:
        mediana = (number_string[int(len(number_string)/2)-1] + number_string[int(len(number_string)/2)])//2

    dictOfModa = dict()
    for key in number_string:
        if key not in dictOfModa:
            dictOfModa[key]=1
        else:
            dictOfModa[key] = dictOfModa[key] + 1

    first_step = False
    
    for key in dictOfModa: #ИСПРАВИТЬ ЕСЛИ НЕТ НАИБОЛЕЕ ЧАСТОГО ВЫДАЕТ ПЕРВОЕ ЧИСЛО, А ДОЛЖНА БЫТЬ ФРАЗА КАКАЯ-НИБУДЬ
        if first_step == False:
            maxim = dictOfModa[key]
            key_max = key
            first_step = True
        else:
            if dictOfModa[key] > maxim:
                maxim = dictOfModa[key]
                key_max = key

    moda=key_max
    
    print(mediana, moda)

    
    
modaAndMediana()
