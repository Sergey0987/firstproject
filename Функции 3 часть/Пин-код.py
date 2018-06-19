def checkPin(pinCode):
    listPin=pinCode.split('-')
    verifyCorrect = []
    rate_of_2 = 2
    for i in range(len(listPin)):
        listPin[i]=int(listPin[i])

    if listPin[0] == 1 or listPin[0] == 2: # Проверка первое число простое
        verifyCorrect.append(True)
    elif listPin[0] > 2:
        count_delenie=0
        for i in range(1,11):
            if listPin[0]%i == 0:
                count_delenie = count_delenie + 1
        if count_delenie <= 2:
            verifyCorrect.append(True)
        else:
            verifyCorrect.append(False)

    
    #Проверка второе число полиндром
    if str(listPin[1]) == str(listPin[1])[::-1]:
        verifyCorrect.append(True)
    else:
        verifyCorrect.append(False)
    

    #Проверка третье число - степень двойки
    while rate_of_2 < listPin[2]:
        rate_of_2 = rate_of_2 * 2
        
    if rate_of_2 == listPin[2]:
        verifyCorrect.append(True)
    else:
        verifyCorrect.append(False)
    

    if False in verifyCorrect:
        print('Некорректен')
    else:
        print('Корректен')




checkPin('7-101-4')
checkPin('12-22-16')


