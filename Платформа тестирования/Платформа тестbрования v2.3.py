#Задача: подготовить систему консольного тестирования сотрудника на 10 вопросов

#FIX:
#Вопросы должны меняться местами от запуска к запуску - fix
#Один верный ответ - один балл - fix
#Вариант реализации: показывается сколько правильных и сколько неправильных ответов дано - fix
#Определение правильного ответа происходит каждый раз при открытии вопрос и ответов к нему. Позволит при перемешивании ответов находить правильный ответ. - fix
#в конце показывать прошел или нет - fix
#система перемешивает ответы - fix
#Возможность использовать вопросы с несколькими вариантами ответа. fix
##Проверку вводимых ответов - введенные значения числа или список чисел - fix


#система должна показывать в каких вопросах была ошибка
#Возможность заливки вопросов в систему через csv или txt
#Нужно чтобы система записывала и хранила результаты прошедшего тестирования


list_of_questions = [[{'Предмет информатики — это': ('язык программирования','устройство робота','способы накопления, хранения, обработки, передачи информации')}],
                     [{'Тройками из нулей и единиц можно закодировать _ различных символов.':(6, 8, 5, 9)}],
                     [{'Капитан спрашивает матроса: «Работает ли маяк?» Матрос отвечает: «То загорается, то погаснет!» Чем является маяк в этой ситуации?':
                       ('Получателем информации','источником информации','каналом связи','помехой')}],
                     [{'В каком веке появились первые устройства, способные выполнять арифметические действия?':('В XVI в.', 'В XVII в.', 'В XVIII в.', 'В XIX в.')}],
                     [{'Механическое устройство, позволяющее складывать числа, изобрел:':('П. Нортон', 'Б. Паскаль', 'Г. Лейбниц', 'Д. Нейман')}],
                     [{'Для какой системы счисления были приспособлены первые семикосточковые счеты?':('Для семеричной', 'для двоичной', 'для десятичной', 'для унарной')}],
                     [{'Выберите все правильные ответы:':('Солнце - светит','Дождь сухой','Курить - вредно','Медведи летают')}]]


dict_of_true_answers = {'Предмет информатики — это': 'способы накопления, хранения, обработки, передачи информации',
                   'Тройками из нулей и единиц можно закодировать _ различных символов.':8,
                   'Капитан спрашивает матроса: «Работает ли маяк?» Матрос отвечает: «То загорается, то погаснет!» Чем является маяк в этой ситуации?':'источником информации',
                   'В каком веке появились первые устройства, способные выполнять арифметические действия?':'В XVII в.',
                   'Механическое устройство, позволяющее складывать числа, изобрел:':'Б. Паскаль',
                   'Для какой системы счисления были приспособлены первые семикосточковые счеты?':'для десятичной', 'Выберите все правильные ответы:':('Солнце - светит','Курить - вредно')}

from random import randrange

def main():
    pass

def sayHelloAskName():
    print('Добро пожаловать в систему тестирования! Как Вас зовут?')
    name = input()
    return name

def chooseQuestions(list_of_questions):
    numbers_of_choose_questions = []
    question_list_for_person = []
    kolichestvo_otbiraemih_voprosof = 3
    while len(numbers_of_choose_questions) != kolichestvo_otbiraemih_voprosof:
        random_number = randrange(0, len(list_of_questions))
        if random_number not in numbers_of_choose_questions:
            numbers_of_choose_questions.append(random_number)
    for i in numbers_of_choose_questions:
        question_list_for_person.append(list_of_questions[i])
    return question_list_for_person

def shuffle_questions(list_of_questions): #ДЕЛАЕМ ПЕРЕМЕШИВАНИЕ СПИСКА ВОПРОСОВ - можно сохранять последнюю комбинацию вопросов и не выдавать такую же (как вариант)
    shuffle_numbers = []
    question_list_for_person = []
    while len(shuffle_numbers) != len(list_of_questions):
        random_number = randrange(0,len(list_of_questions))
        if random_number not in shuffle_numbers:
            shuffle_numbers.append(random_number)
#    print(shuffle_numbers)
    for i in shuffle_numbers:
        question_list_for_person.append(list_of_questions[i])
#    print(question_list_for_person)
    return question_list_for_person


def shuffle_answers_in_questions(list_of_questions):
    for i in range(len(list_of_questions)):
        for j in range(len(list_of_questions[i])):
            for key, values in list_of_questions[i][j].items():
                shuffle_numbers = []
                shuffle_answers = []
                values = list(values)
                while len(shuffle_numbers) != len(values):
                    random_number = randrange(0,len(values))
                    if random_number not in shuffle_numbers:
                        shuffle_numbers.append(random_number)
#                print(shuffle_numbers)
                for t in shuffle_numbers:
                    shuffle_answers.append(values[t])
                values = []
                for k in shuffle_answers:
                    values.append(k)
                list_of_questions[i][j][key] = tuple(values)
    return list_of_questions                




def findTrueAnswer(list_of_questions):
    true_answers_from_selected_questions = []
    for i in range(len(list_of_questions)):
        for j in range(len(list_of_questions[i])):
            for key, values in list_of_questions[i][j].items():
                if type(dict_of_true_answers[key]) != tuple:
                    for number_of_answer in range(len(values)):
                        if values[number_of_answer] == dict_of_true_answers[key]:
                            true_answers_from_selected_questions.append(number_of_answer+1)
                else:
                    true_answers_from_selected_questions.append([])
                    for number_of_answer in range(len(values)):
                        if values[number_of_answer] in dict_of_true_answers[key]:
                            true_answers_from_selected_questions[len(true_answers_from_selected_questions)-1].append(number_of_answer+1)
                            
    return true_answers_from_selected_questions


def sayYourAnswer():
    next_step = False
    while next_step != True:
        next_step = True
        answer = input()
        try:
            answer = int(answer)
        except:
                answer = answer.split()
                for i in range(len(answer)):
                    try:
                        answer[i] = int(answer[i])
                    except:
                        print('Вы ввели недопустимое значение. Введите правильный ответ')
                        next_step = False
    return answer

                

def isYourAnswerTrue(true_answers_from_selected_questions, answer, number_question):
    global counter_of_true_answers
    if type(answer) != type(true_answers_from_selected_questions[number_question - 1]):
        print('Это НЕправильный ответ')
        return
    elif type(answer) != list:
        if true_answers_from_selected_questions[number_question - 1] == answer:
            print('Это правильный ответ!')
            counter_of_true_answers = countTrueAnswers(counter_of_true_answers)
        else:
            print('Это НЕправильный ответ!')
    else:
        count = 0
        count_list = []
        for i in answer:
            if i in true_answers_from_selected_questions[number_question - 1] and i not in count_list:
                count_list.append(i)
                count = count + 1
        if count == len(true_answers_from_selected_questions[number_question - 1]):
            print('Это правильный ответ')
            counter_of_true_answers = countTrueAnswers(counter_of_true_answers)
        else:
            print('Это НЕправильный ответ')

def countTrueAnswers(counter_of_true_answers):
    counter_of_true_answers = counter_of_true_answers + 1
    return counter_of_true_answers

def showResults(counter_of_true_answers):
    print(f'{name}, Вы набрали {counter_of_true_answers} баллов из {len(list_of_questions)}')

# ВОТ ЗДЕСЬ НАЧАЛО ПРОГРАММЫ

list_of_questions = chooseQuestions(list_of_questions)
list_of_questions = shuffle_questions(list_of_questions)
list_of_questions = shuffle_answers_in_questions(list_of_questions)
true_answers_from_selected_questions = findTrueAnswer(list_of_questions)

name = sayHelloAskName()
print(f'{name}, тебе предстоит ответить на несколько вопросов. В тесте их {len(list_of_questions)}! В тесте могут быть вопросы с одним или несколькими вариантами ответа. Если вы считаете, что вариантов ответа несколько, просто укажите их через пробел. Желаем удачи!')
print()

number_question = 1
counter_of_true_answers = 0

for first_level in list_of_questions:
    for second_level in first_level:
        for key_question,spisok_otvetov in second_level.items():
            print(number_question, '.', key_question, sep = '')
            number_vatiant_otveta = 1
            number_of_true_answer = ''
            for variant_otveta in spisok_otvetov:
                print(number_vatiant_otveta,'.', variant_otveta, sep = '')
                number_vatiant_otveta = number_vatiant_otveta + 1
            answer = sayYourAnswer()
            print(answer)
            isYourAnswerTrue(true_answers_from_selected_questions, answer, number_question)
            number_question = number_question + 1
            print()
showResults(counter_of_true_answers)

