#Функция для создания пустого поля 3 на 3
#Функцию вывода поля на экран
#Функция, которая спрашивает у игрока ход и проверяет его корректность
#Функцию, которая изменяет поле в соответствии со сделанным ходом
#Функцию, которая проверяет, есть ли победивший игрок и выводит
#поздравление с победой


def createGameField():
    global gameField
    gameField=[]
    a=[]
    columnAndRowNumber=3
    for i in range(columnAndRowNumber):
        a.append(' ')
    for j in range(columnAndRowNumber):
        gameField.append(a)

def printGameField():
    for i in range(len(gameField)):
        if i == 0:
            print(' - - - -')
        print('|', ' '.join([str(j) for j in gameField[i]]), '|')
    print(' - - - -')



createGameField()
printGameField()

