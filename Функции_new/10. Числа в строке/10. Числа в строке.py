# Напишите функцию fromStringToList(string, container),
# которая принимает два аргумента: строку string и список container.
# string состоит из целых чисел, написанных через пробел.
# Функция должна извлечь из строки числа и добавить их в конец списка

#СДЕЛАЛ ДВУМЯ СПОСОБАМИ НЕ СОВСЕМ ИЗ ЗАДАЧИ ПОНЯТНО, ДОЛЖНА ЛИ СОХРАНЯТЬСЯ
#ИСТОРИЯ СПИСКА

#С СОХРАНЕНИЕМ ИСТОРИИ СПИСКАЮ ПРИ ЗАПУСКЕ НОВОЙ ФУНКЦИИ С НОВЫМИ ЧИСЛАМИ
# ОНИ ДОБАВЛЯЮТСЯ К РАНЕЕ СОЗДАННОМУ СПИСКУ

#def fromStringToList(string, container=[]):
#    a=container
#    string = string.split()
#    for i in string:
#        a.append(int(i))
#    print(a)

#fromStringToList('1 2 3 4 5')
#fromStringToList('4 5 6 7 8')

# ВАРИАНТ ПРОСТО С ОБЫЧНЫМ ИЗВЛЕЧЕНИЕМ ЧИСЕЛ И ДОБАВЛЕНИЕМ В СПИСОК.
# ПЕРЕЗАПУСК ФУНКЦИИ - НОВЫЙ СПИСОК.

def fromStringToList(string, container):
    print(id(container))
    [container.append(int(i)) for i in string.split()]
    print(id(container))
    print(container)

fromStringToList('1 2 3 4 5 6', container=[])

fromStringToList('7 5 6 8 9', container=[])

#ВОПРОС!!!!!!!! ПОЧЕМУ В ДВУХ ПОСЛЕДОВАТЕЛЬНЫХ ФУНКЦИЯХ ID СПИСКА CONTAINER
# ОДИНАКОВЫЙ, ХОТЯ ПО ИДЕЕ, ПЕРЕЗАПУСК ФУНКЦИИ ДОЛЖЕН БЫЛ ОБНУЛИТЬ СТАРЫЙ
