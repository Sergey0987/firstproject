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

    def showMeShip(self):
        print(self.palybs)

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
                        showMeShip()
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
                    self.palybs[x - self.ship_x] == False
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
    def __init__(self, x,y):
        self.x = x
        self.y = y

a = ships(2, 'vf', 5, 3)

print(a.getDammage(5,3))
print(a.getDammage(5,3))

print(a.getDammage(3,3))
print(a.getDammage(6,3))

print(a.getDammage(7,3))
print(a.getDammage(8,3))
