def month(number_of_month, language):
    en_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Dectmber']
    ru_month = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
    if language == 'ru':
        return ru_month[number_of_month - 1]
    else:
        return en_month[number_of_month - 1]


print(month(3, 'ru'))

print(month(4, 'en'))
