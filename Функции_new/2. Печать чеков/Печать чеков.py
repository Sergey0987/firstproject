def addItem(itemName, itemCost, list1=[]):
    list1.append(itemName)
    list1.append(itemCost)
    global a
    a=list1

def printReceipt():
    global a
    global billNumber
    summ=0
    if billNumber==0:
        billNumber=1
    if len(a)>0:
        print("Чек", str(billNumber) + '.', "Всего предметов:", int(len(a)/2))
        for i in range(0,len(a),2):
            print(a[i],"-",a[i+1])
            summ=summ+a[i+1]
        print('Итого: ', summ)
        print('-----')
        billNumber=billNumber+1
    a.clear()

billNumber=0

addItem("Клавиатура", 500)
addItem('Мышь', 300)
addItem('Монитор', 2500)
printReceipt()

printReceipt()

addItem('Кофе', 130)
addItem('Булочка', 50)
printReceipt()

addItem('X-men', 130)
addItem('Deadpool', 50)
printReceipt()
