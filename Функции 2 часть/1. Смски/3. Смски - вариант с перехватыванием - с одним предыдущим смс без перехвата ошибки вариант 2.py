def printWithoutDuplicates(massage, a=[]):
    if massage not in a:
        if len(a)>=1:
            a.pop()
        print(massage)
        a.append(massage) 

     

printWithoutDuplicates('Привет')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Когда доедешь до дома')
printWithoutDuplicates('Ага, жду')
printWithoutDuplicates('Ага, жду')


