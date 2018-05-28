#def setupProfile(name, vacationDate):
#printApplicationForLeave() - заявление на отпуск
#printHolidayMoneyClaim(amount) - выплата отпускных
#printAttorneyLetter(toWhom) - передача своих служебных
#полномочий заместителю

def setupProfile(name, vacationDate, a=[]):
    global profile
    profile=a
    if len(profile)>0:
        profile.clear()
    profile.append(name)
    profile.append(vacationDate)

def printApplicationForLeave():
    if len(profile)>0:
        print('Заявление на отпуск в период', profile[1], '.', profile[0])

def printHolidayMoneyClaim(amount):
    print('Прошу выплатить', amount, 'отпускных денег.', profile[0])

def printAttoneyLetter(toWhom):
    print('На время отпуска в период', profile[1], 'мои заместителем назначается', toWhom, '.', profile[0])


setupProfile('Иван Петров', '1 июня - 20 июня')
printApplicationForLeave()
printApplicationForLeave()
printHolidayMoneyClaim('15 тысяч пиастров')
printAttoneyLetter('Василий Васильев')

setupProfile('Сергей Сергеев', '1 мая - 20 мая')
printApplicationForLeave()
