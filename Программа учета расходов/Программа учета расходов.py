#Программа учета затрат
#Чтобы файл писался по датам и времени и сделать метод, который позволит считать сколько по какому товару мы потратили за любой выбранный период.

import datetime

TYPE_OF_EXPENCE = ['Товар','Услуга']

def verifyIsItInt(number):
    try:
        number = int(number)
        if number < 0:
            return False
        else:
            return number
    except:
        print('Вы ввели не число')
        return False
    

class user:
    def __init__(self, name):
        self.name = name

    def new_purchase(self):  
        type_of_expence = input('Введите тип расходов (Товар или Услуга): ')
        type_of_purchase = input('Введите тип покупки: ')
        purchase_name = input('Введите название товара: ')

        while True:
            volume = verifyIsItInt(input('Введите количество покупок:'))
            if volume != False:
                break

        while True:
            price = verifyIsItInt(input('Введите стоимость товара, в рублях: '))
            if price != False:
                break
            
        new_purchase1 = purchase(type_of_expence, type_of_purchase, purchase_name, volume, price)

        return new_purchase1


    def create_new_basket(self):
        new_basket1 = basket(datetime.date.today())
        return new_basket1
    

class menu:
    def __init__(self, user):
        self.menu_level_1 = ['Просмотреть прошлые покупки', 'Внести в базу новые покупки или расходы', 'Завершить программу']
        self.menu_level_2_1 = ['Посмотреть за дату', 'Посмотреть за период', 'Вернуться на уровень выше']
        self.menu_level_2_2 = ['Внести новый товар\расход', 'Удалить последнее внесение', 'Показать текущий набор покупок\расходов', 'Очистить корзину', 'Записать в файл и закончить', 'Вернуться в уровень выше']
        self.menu_level = self.menu_level_1
        self.user = user

    def verifyPointOfMenu(self, point_of_menu): #часто придется проверять пункт меню, можно сделать отдельной функцией
        try:
            point_of_menu = int(point_of_menu)
        except:
            print('Вы ввели не число')
            return False

        if len(self.menu_level) < point_of_menu or point_of_menu < 1:
            print('Такого пункта нет в меню')
            return False

        return True

    def helloUser(self):
        print(f'Привет, {self.user.name}! Что будем делать?')

    def getUserInputMenuPoint(self):
        point_of_menu = input('Выберите пункт меню: ')
        if self.verifyPointOfMenu(point_of_menu):
            return int(point_of_menu)
        else:
            return -1 # -1 ошибка действие на стороне второго метода

    def selectMenu(self):
        while True:
            result = self.getUserInputMenuPoint()
            if result == -1:
                self.showItemMenu()
            else:
                return result

    def DO(self):
        self.helloUser()
        self.new_basket1 = self.user.create_new_basket()
        while True:
            self.showItemMenu()
            result = self.selectMenu()
            if self.menu_level == self.menu_level_1:
                if self.obrabotka_menu_level_1(result) == -1:
                    break
            elif self.menu_level == self.menu_level_2_1:
                self.obrabotka_menu_level_2_1(result)
            elif self.menu_level == self.menu_level_2_2:
                self.obrabotka_menu_level_2_2(result)

    def obrabotka_menu_level_1(self, point_of_menu):
        if point_of_menu == 1:
            self.menu_level = self.menu_level_2_1
        elif point_of_menu == 2:
            self.menu_level = self.menu_level_2_2
        elif point_of_menu == 3:
            print('Программа завершается')
            return -1

    def obrabotka_menu_level_2_1(self, point_of_menu):
        if point_of_menu == 1:
            self.showDataFromDate()
        elif point_of_menu == 2:
            self.showDataFromInterval()
        elif point_of_menu == 3:
            self.menu_level = self.menu_level_1

    def showDataFromDate(self):
        date = input('Введите дату в формате гггг-мм-дд: ')
        list_of_products = self.findDataInFile(date)
        self.printDataFromFile(list_of_products)

    def findDataInFile(self, date):
        list_of_products = []
        file = open('file.txt', 'r')
        for line in file:
            if date in line:
                list_of_products.append(line)
        return list_of_products

    def printDataFromFile(self, list_of_products):
        for line in list_of_products:
            print(line)

    def showDataFromInterval(self):
        data1 = input('Введите дату в формате гггг-мм-дд, с которой начнем брать данные (включительно): ')
        data2 = input('Введите дату в формате гггг-мм-дд, по которую будем брать данные (включительно): ')
        data_new = purchase_date(data1)
        data1 = data_new.from_string_to_date()
        data_new = purchase_date(data2)
        data2 = data_new.from_string_to_date()
        list_of_products = self.findDataInFileInterval(data1, data2)
        self.printDataFromFile(list_of_products)

    def findDataInFileInterval(self, data1, data2):
        list_of_products = []
        file = open('file.txt', 'r')
        for line in file:
            string_date = self.splitStringFromFile(line)
            data_new = purchase_date(string_date)
            data_new = data_new.from_string_to_date()
            if data_new >= data1 and data_new <= data2:
                list_of_products.append(line)
        return list_of_products
            
    def splitStringFromFile(self, line):
        list_of_line = line.split(' ')
        return list_of_line[0]

    def verifyData1Data2(self, data1, data2):
        list1 = data1.split('-')
        list2 = data1.split('-')
        if len(list1) != 3 or len(list2) != 3:
            print('Вы ввели дату в неверном формате')
            return False

    def varifyYears(self, list1, list2):
        if len(list1[0]) != 4 or len(list2[0]) != 4:
            print('Неверно указан год')
            return False
        try:
            list1[0] = int(list1[0])
        except:
            print('Неправильный формат года')
            return False

        if int(list1[0]) < 1900:
            print('Программа поддерживает даты с 1900 года')
            return False

        if int(list1[0]) > int(list2[0]):
            print('Дата начала больше даты окончания периода! Так не может быть!')
            return False

        return True


    def verifyMonth(self): #запускать проверку месяцев, если года одинаковые; если нет - можно пропустить

        if len(list1[1]) != 2 or len(list2[1]) != 2:
            print('Неверно указан месяц')
            return False

        if len(list1[2]) != 2 or len(list2[2]) != 2:
            print('Неверно указана дата')
            return False

        
        



        if int(list1[0:3]) > int(data2[0:3]):
            return -1

            
        

    def obrabotka_menu_level_2_2(self, point_of_menu):
      
        if point_of_menu == 1:
            new_purchase1 = self.createNewPurchase()
            self.new_basket1.add_purchase_to_basket(new_purchase1)
            
        elif point_of_menu == 2:
            if len(self.new_basket1.basket_list) > 0:
                self.new_basket1.basket_list.pop()
            else:
                print('Корзина и так пуста')
        elif point_of_menu == 3:
            self.new_basket1.showMeAllBasket()
        elif point_of_menu == 4:
            self.new_basket1.basket_list.clear()
        elif point_of_menu == 5:
            self.appendPurchasesInFIle()
        elif point_of_menu == 6:
            self.menu_level = self.menu_level_1

    def appendPurchasesInFIle(self):
        file_of_purchases = open('file.txt', 'a')
        for purchase in self.new_basket1.basket_list:
            string = ''
            string = str(self.new_basket1.day) + ' ' + purchase.type_of_expence + ' ' + purchase.type_of_purchase + ' '  + purchase.name + ' ' + str(purchase.volume) + ' ' + str(purchase.price) + ' ' + '\n'
            file_of_purchases.write(string)
            
        file_of_purchases.close()

    def createNewPurchase(self):
        new_purchase1 = self.user.new_purchase()
        return new_purchase1

    def showItemMenu(self):
        for i in range(1, len(self.menu_level) + 1):
            print(i, self.menu_level[i-1])

    def zapisatInFile(self):
        pass

    def printSummZatrat(self):
        for pokypka in self.basket_list:
            self.summ_zatrat += pokypka.price
        print(self.summ_zatrat)
        

class purchase:
    def __init__(self, type_of_expence, type_of_purchase, name, volume, price):
        self.type_of_expence = type_of_expence
        self.type_of_purchase = type_of_purchase        
        self.name = name
        self.volume = volume       
        self.price = price


class basket:
    def __init__(self, day):
        self.day = day
        self.basket_list = []
        self.summ_zatrat = 0
        
    def add_purchase_to_basket(self, purchase):
        self.basket_list.append(purchase)
        
    def showMeAllBasket(self):
        for pokypka in self.basket_list:
            print(pokypka.type_of_expence, pokypka.type_of_purchase, pokypka.name, pokypka.volume, pokypka.price) 
          
       
    def delLastPurchase(self):
        self.basket_list.pop(len(self.basket_list)-1)

    def clearBasket(self):
        self.basket_list.clear()
        print('Удаление')


class purchase_date:
    def __init__(self, string_date):
        self.string_date = string_date
        
    def from_string_to_date(self):
        date_list = self.string_date.split('-')
        purchase_date_1 = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return purchase_date_1



def main():
    userMe = user('Сергей')
    my_menu = menu(userMe)
    my_menu.DO()
    

  

    
main()



