#Программа учета затрат

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

class menu:
    def __init__(self, controler):
        self.start_menu = ['Войти в систему', 'Создать нового пользователя', 'Выйти из программы']
        self.menu_level_1 = ['Просмотреть прошлые покупки', 'Внести в базу новые покупки или расходы', 'Вернуться в меню выше', 'Завершить программу']
        self.menu_level_2_1 = ['Посмотреть за дату', 'Посмотреть за период', 'Вернуться на уровень выше']
        self.menu_level_2_2 = ['Внести новый товар\расход', 'Удалить товар из корзины', 'Показать текущий набор покупок\расходов', 'Очистить корзину', 'Записать в файл и закончить', 'Вернуться в уровень выше']
        self.menu_level = self.start_menu
        self.controler = controler


#БЛОК МЕТОДОВ ВЫБОРА ПУНКТА МЕНЮ

    def selectMenu(self): #Выбор меню, вызывает getUserInputMenuPoint чтобы получить данные от пользователя
        while True:
            result = self.getUserInputMenuPoint()
            if result == -1:
                self.showItemMenu()
            else:
                return result

    def getUserInputMenuPoint(self): #Запрашивает ввод пункта меню от пользователя и запускает verifyPointOfMenu, чтобы проверить верный ли пункт меню выбран 
        point_of_menu = input('Выберите пункт меню: ')
        if self.verifyPointOfMenu(point_of_menu):
            return int(point_of_menu)
        else:
            return -1 # -1 ошибка действие на стороне второго метода
    
            
    def verifyPointOfMenu(self, point_of_menu): #проверка верно ли выбран пункт меню (число, не вылезает ли за пределы меню)
        try:
            point_of_menu = int(point_of_menu)
        except:
            print('Вы ввели не число')
            return False

        if len(self.menu_level) < point_of_menu or point_of_menu < 1:
            print('Такого пункта нет в меню')
            return False

        return True


    def showItemMenu(self): #аспечатывает пункты текущего уровня меню
        for i in range(1, len(self.menu_level) + 1):
            print(i, self.menu_level[i-1])



#БЛОК МЕНЮ ДЕЛАЙ


    def DO(self):
        while True:
            self.showItemMenu()
            result = self.selectMenu() # Выбрали пункт меню
            if self.menu_level == self.start_menu:
                if self.obrabotka_start_menu(result) == -1:
                    print('Вы вышли из программы!')
                    break
            elif self.menu_level == self.menu_level_1:
                if self.obrabotka_menu_level_1(result) == -1:
                    break
            elif self.menu_level == self.menu_level_2_1:
                self.obrabotka_menu_level_2_1(result)
            elif self.menu_level == self.menu_level_2_2:
                self.obrabotka_menu_level_2_2(result)

#ОБРАБОТКА СТАРТОВОГО МЕНЮ ЗАЛОГИНИВАНИЕ ЮЗЕРА ИЛИ СОЗДАНИЕ ЮЗЕРА
                
    def obrabotka_start_menu(self, point_of_menu):
        if point_of_menu == 1: 
            if self.askLoginPassword() == True:
                self.menu_level = self.menu_level_1
            else:
                print('Такого логина или пароля не существует или неверная пара логин пароль')
        elif point_of_menu == 2:
            if self.createNewUser() == True:
                self.menu_level = self.menu_level_1
        elif point_of_menu == 3:
            return -1

    def askLoginPassword(self):
        login = input('Введите логин')
        password = input('Введите пароль')
        if self.controler.getInformationAboutLoginsAndPasswords(login, password) == True:
            print(f'Здравствуйте, {login}')
            return True
        else:
            return False

    def createNewUser(self):
        login = input('Введите логин')
        password = input('Введите пароль')
        if self.controler.createNewUser(login, password) == True:
            print(f'Здравствуйте, {login}')
            return True
        else:
            print('Попробуйте другой логин, этот занят')
            return False
        
#ОБРАБОТКА ПЕРВОГО МЕНЮ
        
    def obrabotka_menu_level_1(self, point_of_menu):
        if point_of_menu == 1:
            self.menu_level = self.menu_level_2_1
        elif point_of_menu == 2:
            self.menu_level = self.menu_level_2_2
        elif point_of_menu == 3:
            self.menu_level = self.start_menu
        elif point_of_menu == 4:
            print('Программа завершается')
            return -1

#ОБРАБОТКА УРОВНЯ МЕНЮ 2.1

    def obrabotka_menu_level_2_1(self, point_of_menu):
        if point_of_menu == 1:
            self.showDataFromDate()
        elif point_of_menu == 2:
            self.showDataFromInterval() 
        elif point_of_menu == 3:
            self.menu_level = self.menu_level_1


    def showDataFromDate(self):
        date1 = input('Введите дату, гггг--мм-дд: ')
        list_of_purchase = self.controler.showDataFromDate(date1)
        for purchase in list_of_purchase:
            print(purchase)

    def showDataFromInterval(self):
        date1 = input('Введите дату, гггг--мм-дд: ')
        date2 = input('Введите дату, гггг--мм-дд: ')
        list_of_purchase = self.controler.showDataFromInterval(date1, date2)
        for purchase in list_of_purchase:
            print(purchase)        
            
         
#Обработка уровня 2.2 - создание новой покупки        

    def obrabotka_menu_level_2_2(self, point_of_menu):
      
        if point_of_menu == 1:
            new_purchase1 = self.createNewPurchase()
           
        elif point_of_menu == 2:
            self.deletePurchase()
        elif point_of_menu == 3:
            self.showMeAllBaskets()
        elif point_of_menu == 4:
            self.clear_basket()
        elif point_of_menu == 5:
            self.appendPurchasesInFIle()
        elif point_of_menu == 6:
            self.menu_level = self.menu_level_1


    def createNewPurchase(self):
        basket_name = input('Введите название магазина: ')
        day_of_purchase = datetime.date.today()
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
            
        new_purchase1 = self.controler.new_purchase(basket_name, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price)

    def deletePurchase(self):
        basket_name = input('Введите название магазина откуда удалить покупку')
        purchase_name = input('Введите название товара для удаления: ')
        self.controler.delPurchase(basket_name, purchase_name)

    def showMeAllBaskets(self):
        temp_data = self.controler.showMeAllBaskets()
        print('Название магазина ' + 'День покупки ' + 'Тип расходов ' + 'Тип покупки ' + 'Название покупки ' + 'Количество покупок ' + 'Цена ')
        for line in temp_data:
            print(line)

    def clear_basket(self):
        basket_name = input('Введите название магазина, корзину которого нужно удалить (или введите all - чтобы очистить все корзины)')
        if self.controler.clear_basket(basket_name) == True:
            print('Данные удалены')
        else:
            print('Нельзя удалить несуществующие данные')

    def appendPurchasesInFIle(self):
        if self.controler.appendPurchasesInFIle() == True:
            print('Данные записаны')
        else:
            print('Данные нельзя записать')
        


class controler:
    def __init__(self, model):
        self.model = model

    def new_purchase(self, basket_name, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price):            
        new_purchase1 = self.model.create_purchase(basket_name, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price)
 

    def getInformationAboutLoginsAndPasswords(self, login, password):
        if self.model.getInformationAboutLoginsAndPasswords(login, password) == True:
            return True
        else:
            return False

    def createNewUser(self, login, password):
        if self.model.create_user(login, password) == True:
            return True
        else:
            return False

    def delPurchase(self, basket_name, purchase_name):
        self.model.deletePurchase(basket_name, purchase_name)

    def showMeAllBaskets(self):
        temp_data = self.model.showMeAllBaskets()
        return temp_data

    def clear_basket(self, basket_name):
        if self.model.clear_basket(basket_name) == True:
            return True
        else:
            return False

    def appendPurchasesInFIle(self):
        if self.model.appendPurchasesInFIle() == True:
            return True
        else:
            return False

    def showDataFromDate(self, date1):
        return self.model.showDataFromDate(date1)

    def showDataFromInterval(self, date1, date2):
        return self.model.showDataFromInterval(date1, date2)


class Model:
    def __init__(self):
        self.users = dict()
        self.users_log_pass = dict()


    def download_users_log_pass(self):
        log_pass = open('loginpassword.txt', 'r')
        for line in log_pass:
            line = line.split()
            user_name = line[0]
            password = line[1]
            userMe = User(user_name, password)
            self.users_log_pass[user_name] = userMe
        
    def create_user(self, user_name, password):
        log_pass = open('loginpassword.txt', 'r')
        for line in log_pass:
            line = line.split()
            if line[0] == user_name:
                return False
        log_pass = open('loginpassword.txt', 'a')
        log_pass.write(str(user_name) + ' ' + str(password) + '\n')
        log_pass.close()
        self.userMe = User(user_name, password)
        self.users[user_name] = self.userMe
        return True

    def getInformationAboutLoginsAndPasswords(self, user_name, password):
        if user_name in self.users_log_pass:
            if password == self.users_log_pass[user_name].password:
                self.userMe = User(user_name, password)
                return True
            else:
                return False
        else:
            return False

    def create_purchase(self, basket_name, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price): 
        self.userMe.create_purchase(basket_name, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price)


    def deletePurchase(self, basket_name, purchase_name):
        self.userMe.deletePurchase(basket_name, purchase_name)

    
    def showMeAllBaskets(self):
        temp_data = self.userMe.showMeAllBaskets()
        return temp_data

    def clear_basket(self, basket_name):
        if self.userMe.clear_basket(basket_name) == True:
            return True
        else:
            return False

    def appendPurchasesInFIle(self):
        if self.userMe.appendPurchasesInFIle() == True:
            return True
        else:
            return False

    def showDataFromDate(self, date1):
        return self.userMe.showDataFromDate(date1)

    def showDataFromInterval(self, date1, date2):
        return self.userMe.showDataFromInterval(date1, date2)


class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.baskets = dict()

    def create_purchase(self, basket_name, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price):
        if basket_name not in self.baskets:
            self.create_basket(basket_name)
            self.baskets[basket_name].create_purchase(day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price)
        else:
            self.baskets[basket_name].create_purchase(day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price)
    
    def create_basket(self, basket_name):
        new_basket = basket(basket_name)
        self.baskets[basket_name] = new_basket

    def del_basket(self, basket_name):
        if basket_name in self.baskets:
            del self.baskets[basket_name]
            return True
        else:
            return False

    def deletePurchase(self, basket_name, purchase_name):
        if basket_name in self.baskets:
            if purchase_name in self.baskets[basket_name].basket_list:
                self.baskets[basket_name].delPurchase(purchase_name)
                if len(self.baskets[basket_name].basket_list) == 0:
                    self.del_basket(basket_name)
            else:
                return False
        else:
            return False

    def showMeAllBaskets(self):
        list_of_all_purchase = self.merge_in_one_list_all_purchases()
        return list_of_all_purchase

    def merge_in_one_list_all_purchases(self):
        list_of_all_purchase = []
        for basket_names_key in self.baskets:
            for purchase_names_key in self.baskets[basket_names_key].basket_list:
                list_of_all_purchase.append((basket_names_key + ' ' + str(self.baskets[basket_names_key].basket_list[purchase_names_key].day_of_purchase) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].type_of_expence) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].type_of_purchase) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].purchase_name) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].volume) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].price)))
        return list_of_all_purchase        


    def clear_basket(self, basket_name):
        if basket_name == 'all':
            self.baskets.clear()
            return True
        else:
            if basket_name in self.baskets:
                self.baskets[basket_name].basket_list.clear()
                return True
            else:
                return False

    def appendPurchasesInFIle(self):
        if len(self.baskets) > 0:
            list_of_all_purchase = self.merge_in_one_list_all_purchases2() 
            file = open('file.txt', 'a')
            for purchase in list_of_all_purchase:
                file.write(purchase + '\n')
            file.close()
            return True
        else:
            return False

    def merge_in_one_list_all_purchases2(self): #вторая версия для записи с юзер неймом
        list_of_all_purchase = []
        for basket_names_key in self.baskets:
            for purchase_names_key in self.baskets[basket_names_key].basket_list:
                list_of_all_purchase.append((self.user_name + ' ' + basket_names_key + ' ' + str(self.baskets[basket_names_key].basket_list[purchase_names_key].day_of_purchase) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].type_of_expence) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].type_of_purchase) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].purchase_name) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].volume) + ' ' +
                             str(self.baskets[basket_names_key].basket_list[purchase_names_key].price)))
        return list_of_all_purchase    

    def showDataFromDate(self, date1):
        date1 = self.translation_from_string_to_date(date1)
        data_from__date = self.download_data_from_date(date1)
        return data_from__date

    def translation_from_string_to_date(self, date1):
        date1 = date1.split('-')
        date1 = datetime.date(int(date1[0]),int(date1[1]),int(date1[2]))
        return date1

    def download_data_from_date(self, date1):
        list_of_all_purchase_from_date = []
        file = open('file.txt', 'r')
        for line in file:
            list_of_purchase = line.split()
            date2 = self.translation_from_string_to_date(list_of_purchase[2])
            if date1 == date2 and list_of_purchase[0] == self.user_name:
                index1 = line.find('\n')
                list_of_all_purchase_from_date.append(line[:index1])
        file.close()
        return list_of_all_purchase_from_date

    def showDataFromInterval(self, date1, date2):
        date1 = self.translation_from_string_to_date(date1)
        date2 = self.translation_from_string_to_date(date2)
        data_from_interval = self.download_data_from_interval(date1, date2)
        return data_from_interval

    def download_data_from_interval(self, date1, date2):
        list_of_all_purchase_from_date = []
        file = open('file.txt', 'r')
        for line in file:
            list_of_purchase = line.split()
            date3 = self.translation_from_string_to_date(list_of_purchase[2])
            if date1 <= date3 and date3 <= date2 and list_of_purchase[0] == self.user_name:
                index1 = line.find('\n')
                list_of_all_purchase_from_date.append(line[:index1])
        file.close()
        return list_of_all_purchase_from_date        
    


class basket:
    def __init__(self, day):
        self.day = day
        self.basket_list = dict()
        self.summ_zatrat = 0
        self.last_pokypka = 0
        

    def create_purchase(self, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price): 
        new_purchase = purchase(day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price)
        self.basket_list[purchase_name] = new_purchase
        print(self.basket_list)

    def delPurchase(self, purchase_name):
        print(self.basket_list)
        del self.basket_list[purchase_name]



class purchase:
    def __init__(self, day_of_purchase, type_of_expence, type_of_purchase, purchase_name, volume, price):
        self.day_of_purchase = day_of_purchase
        self.type_of_expence = type_of_expence
        self.type_of_purchase = type_of_purchase        
        self.purchase_name = purchase_name
        self.volume = volume       
        self.price = price


def main():
    my_model = Model()
    my_model.download_users_log_pass()
    controlerMe = controler(my_model)
    my_menu = menu(controlerMe)
    my_menu.DO()
    

  

    
main()



