def printWithoutDuplicates(massage):  
    global b
    try:
        if massage != b:
            b=massage
            print(b)
    except NameError:
        b=massage
        print(b)


        

printWithoutDuplicates('Привет')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Когда доедешь до дома')
printWithoutDuplicates('Ага, жду')
printWithoutDuplicates('Ага, жду')


