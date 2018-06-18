def addFriends(nameOfPerson, listOfFriends):
    global dictOfFriends
    dictOfFriends[nameOfPerson] = listOfFriends


def isFriends(nameOfPerson1, nameOfPerson2):
    friends1, friends2 = False, False
    
    if nameOfPerson2 in dictOfFriends:
        if nameOfPerson1 in dictOfFriends[nameOfPerson2]:
            friends1=True

    if nameOfPerson1 in dictOfFriends:
        if nameOfPerson2 in dictOfFriends[nameOfPerson1]:
            friends2=True

    if friends1 == True or friends2 == True:
        print(True)
    else:
        print(False)

def printFriends(nameOfPerson):
    for i in dictOfFriends[nameOfPerson]:
        print(i, end = ' ')



dictOfFriends=dict()
addFriends('Вася', ['Катя', 'Даша', 'Петя'])
addFriends('Роберт',['Наташа'])
isFriends('Вася','Катя')
isFriends('Вася','Роберт')
printFriends('Вася')
