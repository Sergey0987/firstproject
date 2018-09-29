class ships:
    HIT = 1
    MISS = 0
    KILL = -1
    DOUBLE_HIT = 2
    
    def __init__(self, number_of_palybs, raspolozhen, x, y):
        self.number_of_palybs = number_of_palybs
        self.palybs = [True]*number_of_palybs
        self.raspolozhen = raspolozhen
        self.ship_x = x
        self.ship_y = y

    def __isKillShip(self):
        for i in self.palybs:
            if i == True:
                return False
        return True

    def getMyPalybs(self):
        return self.palybs

    def getDammage(self, x,y):
        if self.raspolozhen == 'v':
            return self.__getDammageVetrical(x, y)
        else:
            return self.__getDammageHorizont(x, y)

    
    def __getDammageVetrical(self, x, y):
            if self.ship_x == x:
                if y >= self.ship_y and y < (self.ship_y + self.number_of_palybs):
                    if self.palybs[y - self.ship_y] == True:
                        self.palybs[y - self.ship_y] = False
                        if self.__isKillShip() == True:
                            return self.KILL
                        else:
                            return self.HIT
                    else:
                        return self.DOUBLE_HIT
                else:
                    return self.MISS
                    
            else:
                return self.MISS

    def __getDammageHorizont(self, x,y):
        if self.ship_y == y:
            if x >= self.ship_x and x < (self.ship_x + self.number_of_palybs):
                if self.palybs[x - self.ship_x] == True:
                    self.palybs[x - self.ship_x] = False
                    if self.__isKillShip() == True:
                        return self.KILL
                    else:
                        return self.HIT
                else:
                    return self.DOUBLE_HIT
            else:
                return self.MISS
        else:
            return self.MISS

class field:
    ALL_IS_OK = 0
    ERROR_COUNT_PALYBS = 1
    ERROR_LIMIT_SHIPS = 2
    ERROR_SHIP_OUT_OF_FIELD = 3
    ERROR_SHIP_OVERLAP_ANOTHER_SHIP = 4
    NEXT_STEP = 5
    STEP_ANOTHER_PLAYER = 6
    
    def __init__(self, x,y, dictionary_of_ships): #dictionary_of_ships - словарь в котором есть указание сколько n-палубных кораблей (ключ) может располагаться на поле (значение по ключу)
        self.size_x = x
        self.size_y = y
        self.list_of_ships = []
        self.dictionary_of_ships = dictionary_of_ships

    def addShip(self, ship):
        if len(ship.palybs) not in self.dictionary_of_ships:
            print('ERROR_COUNT_PALYBS')
            return self.ERROR_COUNT_PALYBS

        if self.dictionary_of_ships[len(ship.palybs)] <= 0:
            print('ERROR_LIMIT_SHIPS')
            return self.ERROR_LIMIT_SHIPS

        if self.__isShipInField() != 0:
            print('ERROR_SHIP_OUT_OF_FIELD')
            return self.ERROR_SHIP_OUT_OF_FIELD

        if self.__isShipOverlapAnotherShip() == 4:
            print('ERROR_SHIP_OVERLAP_ANOTHER_SHIP')
            return self.ERROR_SHIP_OVERLAP_ANOTHER_SHIP
        else:
            self.list_of_ships.append(ship)
            self.dictionary_of_ships[len(ship.palybs)] = self.dictionary_of_ships[len(ship.palybs)] - 1
#            print(self.dictionary_of_ships[len(ship.palybs)])


    def __isShipInField(self):
        if ship.ship_x > self.size_x or ship.ship_y > self.size_y:
            return self.ERROR_SHIP_OUT_OF_FIELD
        
        if ship.raspolozhen == 'v':
            if ship.ship_y + len(ship.palybs) > self.size_y:
                return self.ERROR_SHIP_OUT_OF_FIELD
            else:
                return self.ALL_IS_OK
        else:
            if ship.ship_x + len(ship.palybs) > self.size_x:
                return self.ERROR_SHIP_OUT_OF_FIELD
            else:
                return self.ALL_IS_OK


    def __isShipOverlapAnotherShip(self):
        if len(self.list_of_ships) == 0:
            return self.ALL_IS_OK
        else:
            for ship_from_list_of_ships in self.list_of_ships:
                if ship_from_list_of_ships.ship_x == ship.ship_x and ship_from_list_of_ships.ship_y == ship.ship_y:
                    return self.ERROR_SHIP_OVERLAP_ANOTHER_SHIP

                if ship_from_list_of_ships.raspolozhen == 'v':
                    ax = ship_from_list_of_ships.ship_x - 1
                    ay = ship_from_list_of_ships.ship_y + ship_from_list_of_ships.number_of_palybs

                    bx = ship_from_list_of_ships.ship_x - 1
                    by = ship_from_list_of_ships.ship_y - 1

                    cx = ship_from_list_of_ships.ship_x + 1
                    cy = ship_from_list_of_ships.ship_y - 1
                else:
                    ax = ship_from_list_of_ships.ship_x - 1
                    ay = ship_from_list_of_ships.ship_y + 1

                    bx = ship_from_list_of_ships.ship_x - 1
                    by = ship_from_list_of_ships.ship_y - 1

                    cx = ship_from_list_of_ships.ship_x + ship_from_list_of_ships.number_of_palybs
                    cy = ship_from_list_of_ships.ship_y - 1                    

                if ship.ship_x >= bx and ship.ship_x <= cx and ship.ship_y >= by and ship.ship_y <= ay: #проверка точки, от которой начинается корабль (первая палуба)
                    return self.ERROR_SHIP_OVERLAP_ANOTHER_SHIP

                if ship.raspolozhen == 'v':  # проверка точки, которой заканчивается корабль (последняя палуба). Если есть пересечение, то или первая или последняя палуба попадет под условие
                    if ship.ship_x >= bx and ship.ship_x <= cx and ship.ship_y + (len(ship.palybs) - 1) >= by and ship.ship_y + (len(ship.palybs) - 1) <= ay:
                        return self.ERROR_SHIP_OVERLAP_ANOTHER_SHIP
                else:
                    if ship.ship_x + (len(ship.palybs) - 1) >= bx and ship.ship_x + (len(ship.palybs) - 1) <= cx and ship.ship_y >= by and ship.ship_y <= ay:
                        return self.ERROR_SHIP_OVERLAP_ANOTHER_SHIP
                
            return self.ALL_IS_OK

    def shot_in_field(self, x, y):
        for ship in self.list_of_ships:
            result = ship.getDammage(x,y)
            if result == 1:
                print('Попадание')
                return self.NEXT_STEP
            elif result == -1:
                print('Корабль потоплен!')
                return self.NEXT_STEP
        print('Мимо, ход другого игрока')
        return self.STEP_ANOTHER_PLAYER

                
    def showMeField(self):
        print(self.list_of_ships)
                
#class showDataShip():
#    def __init__(self, a):
#        self.a = a
#    def getDammage(self, x,y):
#        print(a.getDammage(x,y))
#        print(a.getMyPalybs())

#b = showDataShip(ship)

#b.getDammage(5,3)

ship = ships(2, 'v', 2, 3)

field_1 = field(10, 10, {2:1, 3:2, 4:1})

field_1.addShip(ship)
field_1.showMeField()

field_1.shot_in_field(2, 3)
field_1.shot_in_field(2, 1)
