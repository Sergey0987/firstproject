def little_frequency_analysis():
    string = input()
    dictOfFrequency = dict()
    for i in string:
        if i not in dictOfFrequency and i != ' ':
            dictOfFrequency[i] = 1
        else:
            dictOfFrequency[i] = dictOfFrequency[i] + 1
    print(dictOfFrequency)

    next_step = False
    for i in dictOfFrequency:
        if next_step == False:
            maxim = dictOfFrequency[i]
            next_step = True
            key = i 
        else:
            if dictOfFrequency[i] > maxim:
                maxim = dictOfFrequency[i]
                key = i
    print('Самый частый символ в строке ' + key + '=' + str(dictOfFrequency[key]))

little_frequency_analysis()
