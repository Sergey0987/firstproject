def printWithoutDuplicates(massage, a=[]):
    global lastMessage
    if lastMessage!= massage:
        print(massage)
    lastMessage=massage

     
lastMessage = ""
printWithoutDuplicates('Привет')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Не могу до тебя дозвониться')
printWithoutDuplicates('Когда доедешь до дома')
printWithoutDuplicates('Ага, жду')
printWithoutDuplicates('Ага, жду')


