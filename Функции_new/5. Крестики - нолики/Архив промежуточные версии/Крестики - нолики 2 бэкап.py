#Функция для создания пустого поля 3 на 3
#Функцию вывода поля на экран
#Функция, которая спрашивает у игрока ход и проверяет его корректность
#Функцию, которая изменяет поле в соответствии со сделанным ходом
#Функцию, которая проверяет, есть ли победивший игрок и выводит
#поздравление с победой

#ДОДЕЛАТЬ
#Если поля все заняты и никто не выйграл сделать проверку
#Если ввели не то значение в координаты
#Если ввели только одну координату


def createGameField():
    global gameField
    global win
    win = 0
    gameField=[]
    a=[]
    columnAndRowNumber=3
    for i in range(columnAndRowNumber):
        a.append('.')
    for j in range(columnAndRowNumber):
        gameField.append(a[:])
    global firstSymbol
    firstSymbol = 'X'

def printGameField():
    global gameField
    for t in gameField:
        for q in t:
            print(q, end = ' ')
        print()
    

def doStep():
    global step
    global firstSymbol
    step=[]
    step = [int(z)-1 for z in input('Делаете ход! Введите номер строки и столбца через пробел: ').split()]
    while step[0]>2 or step[1]>2 or step[0] < 0 or step[1] < 0:
        step.clear()
        print('Вы ввели координаты за пределами игрового поля!')
        step=[int(z)-1 for z in input('Давайте, попробуем еще раз! Введите номер строки и столбца через пробел: ').split()]
    
    while gameField[step[0]][step[1]] != '.':
        step.clear()
        print('Это поле уже занято. Пожалуйста, выберите другое!')
        step=[int(g)-1 for g in input('Давайте, попробуем еще раз! Введите номер строки и столбца через пробел: ').split()]
#    print(step)

         
def changeField(gameField):
    global step
    global firstSymbol
    gameField[step[0]][step[1]] = firstSymbol
    if firstSymbol == 'X':
        firstSymbol = '0'
    elif firstSymbol == '0':
        firstSymbol = 'X'


def winnerVerify():
    global summMainDiagonal
    ord_X = 88
    ord_0 = 48
    controlSummX=ord_X*3
    controlSumm0=ord_0*3
    summVertical=0
    summGorizontal=0
    summMainDiagonal=0
    summDopolnitDiagonal=0
    global win
    for i in range(len(gameField)):
        for j in range(len(gameField)):
            summVertical=summVertical+ord(gameField[j][i])
            summGorizontal=summGorizontal+ord(gameField[i][j])
        if summVertical == controlSummX or summGorizontal == controlSummX or summMainDiagonal == controlSummX or summDopolnitDiagonal == controlSummX:
                   print('Играющий за X победил! Поздравляем вас!!!')
                   win = 1
                   break
        elif summVertical == controlSumm0 or summGorizontal == controlSumm0 or summMainDiagonal == controlSumm0 or summDopolnitDiagonal == controlSumm0:
                   print('Играющий за 0 победил! Поздравляем вас!!!')
                   win = 1
                   break
        summVertical=0
        summGorizontal=0

    for i in range(len(gameField)):
        for j in range(len(gameField)):
            if i == j:
                summMainDiagonal = summMainDiagonal + ord(gameField[i][j])
            elif i+j == 2:
                summDopolnitDiagonal = summDopolnitDiagonal + ord(gameField[i][j])
        if summMainDiagonal == controlSummX or summDopolnitDiagonal == controlSummX:
            print('Играющий за X победил! Поздравляем вас!!!')
            win = 1
        elif summMainDiagonal == controlSumm0 or summDopolnitDiagonal == controlSumm0:
            win = 1
            print('Играющий за 0 победил! Поздравляем вас!!!')

    for i in gameField:
        for j in i:
            if j == '.':
                win = 0


createGameField()
printGameField()
while win != 1:
    doStep()
    changeField(gameField)
    printGameField()
    winnerVerify()




