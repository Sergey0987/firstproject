#Задача: подготовить систему консольного тестирования сотрудника на 10 вопросов
#Вопросы должны меняться местами от запуска к запуску
#Один верный ответ - один балл , система должна запоминать данные ответы
#и в конце показывать прошел или нет и в каких вопросах была ошибка

#Вариант реализации: показывается сколько правильных и сколько неправильных ответов дано
#Определение правильного ответа происходит каждый раз при открытии вопрос и ответов к нему. Позволит при перемешивании ответов находить правильный ответ.

list_of_questions = [[{'Предмет информатики — это': ('язык программирования','устройство робота','способы накопления, хранения, обработки, передачи информации')}],
                     [{'Тройками из нулей и единиц можно закодировать _ различных символов.':(6, 8, 5, 9)}],
                     [{'Капитан спрашивает матроса: «Работает ли маяк?» Матрос отвечает: «То загорается, то погаснет!» Чем является маяк в этой ситуации?':('Получателем информации','источником информации','каналом связи','помехой')}]]


dict_of_true_answers = {'Предмет информатики — это': 'способы накопления, хранения, обработки, передачи информации',
                   'Тройками из нулей и единиц можно закодировать _ различных символов.':8,
                   'Капитан спрашивает матроса: «Работает ли маяк?» Матрос отвечает: «То загорается, то погаснет!» Чем является маяк в этой ситуации?':'источником информации'}

def main():
    pass
            
def chooseQuestions():
    pass

def sayYourAnswer():
    pass

def findTrueAnswer(key_question, variant_otveta, number_vatiant_otveta, number_of_true_answer): #key_question - сам вопрос
    if variant_otveta == dict_of_true_answers[key_question]:
        number_of_true_answer = number_vatiant_otveta        
#        print(variant_otveta, dict_of_true_answers[key_question], number_vatiant_otveta, number_of_true_answer)
        return number_of_true_answer
    else:
        return number_of_true_answer

    

def isYourAnswerTrue(number_of_true_answer, answer):
    if number_of_true_answer == answer:
        print('Это правильный ответ!')
    else:
        print('Это НЕправильный ответ!')

def countTrueAnswers(counter_of_true_answers):
    pass

def showResults():
    pass


number_question = 1
counter_of_true_answers = 0

for first_level in list_of_questions:
    for second_level in first_level:
        for key_question,spisok_otvetov in second_level.items():
            print(number_question, key_question)
            number_question = number_question + 1
            number_vatiant_otveta = 1
            number_of_true_answer = ''
            for variant_otveta in spisok_otvetov:
                print(number_vatiant_otveta,'.', variant_otveta, sep = '')
                if number_of_true_answer == '':
                    number_of_true_answer = findTrueAnswer(key_question, variant_otveta, number_vatiant_otveta, number_of_true_answer)
                number_vatiant_otveta = number_vatiant_otveta + 1
#            print(number_of_true_answer)
            answer = int(input('Введите номер ответа: '))
#            print(answer, number_of_true_answer)
            isYourAnswerTrue(number_of_true_answer, answer)
            print()


