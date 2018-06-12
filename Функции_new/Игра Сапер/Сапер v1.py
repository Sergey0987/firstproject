# Сапер
# Функция создание поля с указанием положения бомб
# Функция печати поля
# Функция проверки есть ли рядом бомбы

#Сделать функцию проверка бомб с ограничением количества попыток 

def create_field():
    next_step = False
    while next_step != True:
        next_step = True
        Fields=input('Введите количество полей для игры, от 2-х до 20: ')
        try:
            Fields = int(Fields)           
        except ValueError:
            print('Вы ввели не число. Давайте еще раз!')
            next_step = False

        if next_step == True:        
            if Fields < 2 or Fields > 20:
                next_step = False
                print('Вы ввели число не в диапазоне от 2-х до 20. Давайте еще раз!')

    if next_step == True:                    
        global gameField
        global visibleGameField
        global win
        win = 0
        gameField=[]
        visibleGameField=[]
        for i in range(Fields):
            gameField.append([])
            visibleGameField.append([])
            for j in range(Fields):
                visibleGameField[i].append('.')
                gameField[i].append('.')

def print_game_field():
    for i in gameField:
        for j in i:
            print(j, end= ' ')
        print()

def print_visible_game_field():
    for i in visibleGameField:
        for j in i:
            print(j, end = ' ')
        print()


def instal_bombs():
    import random
    global gameField
    bombs=random.randrange(len(gameField)//3, len(gameField)*2)
    bombCoordinate = []
    NUMBERS_OF_ONE_BOMB_COORDINATE = 2
    for i in range(bombs*NUMBERS_OF_ONE_BOMB_COORDINATE):
        bombCoordinate.append(random.randrange(0,len(gameField)-1))
#    print('bombs = ', bombs)
#    print('bombCoordinate= ', bombCoordinate)

    for i in range(0, len(bombCoordinate), 2):
        gameField[bombCoordinate[i]][bombCoordinate[i+1]]='b'

def proverka_i0_j0(i,j):
    global gameField
    a=0
    if i==0 and j==0:
        if gameField[i+1][j+1]=='b':
            a=a+1
        if gameField[i+1][j]=='b':
            a=a+1
        if gameField[i][j+1]=='b':
            a=a+1
        gameField[0][0]=a

def proverka_i0(i,j):
    global gameField
    a=0
    if (i==0 and j != 0 and j != (len(gameField) - 1)):
        if gameField[i][j-1] == 'b':
            a=a+1
        if gameField[i+1][j-1] == 'b':
            a=a+1
        if gameField[i+1][j] == 'b':
            a=a+1
        if gameField[i][j+1] == 'b':
            a=a+1
        if gameField[i+1][j+1] == 'b':
            a=a+1
        gameField[i][j] = a

def proverka_i0_j_len_list1i_minus_1(i,j):
    global gameField
    a=0
    if i == 0 and j == (len(gameField[i])-1):
        if gameField[i][j-1] == 'b':
            a=a+1
        if gameField[i-1][j-1] == 'b':
            a=a+1
        if gameField[i-1][j] == 'b':
            a=a+1
        gameField[i][j] = a

def proverka_j_list1i_minus_1(i,j):
    global gameField
    a = 0
    if i != 0 and j == len(gameField[i])-1 and i != len(gameField[i])-1:
        if gameField[i-1][j] == 'b':
            a=a+1
        if gameField[i-1][j-1] == 'b':
            a=a+1
        if gameField[i][j-1] == 'b':
            a=a+1
        if gameField[i+1][j-1] == 'b':
            a=a+1
        if gameField[i+1][j] == 'b':
            a=a+1
        gameField[i][j] = a

def proverka_ilenlist1minus1_jlenlist1minus1(i,j):
    global gameField
    a=0
    if i == len(gameField)-1 and j == len(gameField)-1:
        if gameField[i][j-1] == 'b':
            a=a+1
        if gameField[i-1][j-1] == 'b':
            a=a+1
        if gameField[i-1][j] == 'b':
            a=a+1
        gameField[i][j] = a
            
def ilenlist1minus1(i,j):
    global gameField
    a=0
    if (i == len(gameField)-1 and j != 0 and j != len(gameField) - 1):
        if gameField[i][j-1] == 'b':
            a=a+1
        if gameField[i-1][j-1] == 'b':
            a=a+1
        if gameField[i-1][j] == 'b':
            a=a+1
        if gameField[i-1][j+1] == 'b':
            a=a+1
        if gameField[i][j+1] == 'b':
            a=a+1
        gameField[i][j] = a
            

def ilenlist1minus1_j0(i,j):
    global gameField
    a=0
    if i == len(gameField)-1 and j == 0:
        if gameField[i-1][j] == 'b':
            a = a + 1
        if gameField[i-1][j+1] == 'b':
            a = a + 1
        if gameField[i][j+1] == 'b':
            a = a + 1
        gameField[i][j] = a


def j0(i,j):
    global gameField
    a = 0
    if (i != 0 and j == 0 and i != len(gameField)-1):
        if gameField[i-1][j] == 'b':
            a = a + 1
        if gameField[i-1][j+1] == 'b':
            a = a +1
        if gameField[i][j+1] == 'b':
            a = a +1
        if gameField[i+1][j+1] == 'b':
            a = a + 1
        if gameField[i+1][j] == 'b':
            a = a + 1
        gameField[i][j] = a

def ij_inside(i,j):
    global gameField
    a=0
    if i!=0 and j!=0 and i != len(gameField)-1 and j != len(gameField[i])-1:
        if gameField[i][j-1] == 'b':
            a=a+1
        if gameField[i+1][j-1] == 'b':
            a=a+1
        if gameField[i+1][j] == 'b':
            a=a+1
        if gameField[i][j+1] == 'b':
            a=a+1
        if gameField[i+1][j+1] == 'b':
            a=a+1
        if gameField[i-1][j-1] == 'b':
            a=a+1
        if gameField[i-1][j] == 'b':
            a=a+1
        if gameField[i-1][j+1] == 'b':
            a=a+1
        gameField[i][j] = a
  


def instal_podskaz():
    global gameField
    for i in range(len(gameField)):
        for j in range(len(gameField[i])):
            if gameField[i][j] != 'b':
#                print(i,j)
                proverka_i0_j0(i,j)
                proverka_i0(i,j)
                proverka_i0_j_len_list1i_minus_1(i,j)
                proverka_j_list1i_minus_1(i,j)
                proverka_ilenlist1minus1_jlenlist1minus1(i,j)
                ilenlist1minus1(i,j)
                ilenlist1minus1_j0(i,j)
                j0(i,j)
                ij_inside(i,j)
                

def do_step(list1=[]):
    global gameField
    global visibleGameField
    global end
    global win
    bomb_explosion = 0
    step=list1
    step.clear()
    next_step = False

    while next_step != True:
        
        step=[i for i in input('Введите координаты: ').split()]
        next_step = True

        if len(step) < 2:
            next_step = False
            print('Вы ввели меньше 2 координат. Давайте еще раз!')

        if len(step) > 2:
            next_step = False
            print('Вы ввели больше 2 координат. Давайте еще раз!')

        if next_step == True:
            try:
                for i in range(len(step)):
                    step[i]=int(step[i])
            except ValueError:
                next_step = False
                print('Координаты должны быть цифрами не меньше 1 и не больше ' + str(len(gameField)) + '. Давайте еще раз')

        if next_step == True:    
            for i in range(len(step)):
                if step[i]<1 or step[i]>len(gameField):
                    next_step = False
            if next_step == False:
                print('Координаты не могут быть меньше 1 или больше ' + str(len(gameField)) + '. Давайте еще раз!')
                
        
            
    for i in range(len(step)):
        if int(step[i]) == 0:
            step[i] = int(step[i])
        else:
            step[i]=int(step[i])-1
            
    if gameField[step[0]][step[1]] == 'b':
        visibleGameField[step[0]][step[1]] = gameField[step[0]][step[1]]
        print('Бабах!!! Вы взорвали бомбу и проиграли!!!')
        print_game_field()
        bomb_explosion = 1
        win = 1
    else:
        visibleGameField[step[0]][step[1]] = gameField[step[0]][step[1]]

def verify_winner():
    global gameField
    global visibleGameField
    verify=0
    if bomb_explosion == 0:
        win = 1
        for i in range(len(visibleGameField)):
            for j in range(len(visibleGameField[i])):
                if visibleGameField[i][j] == '.' and gameField[i][j] != 'b':
                    verify = verify + 1
                    win = 0

#Логика
#create_field()
#instal_bombs()
#instal_podskaz()

create_field()
print_game_field()
instal_bombs()
instal_podskaz()

while win != 1:            
    do_step(list1=[])
    print_visible_game_field()
    verify_winner
    print()
#    print_game_field()


