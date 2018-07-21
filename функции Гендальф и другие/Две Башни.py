def createListOfProduct():
    list_of_products = []
    list_of_names = []
    counter = 0
    while counter != 1:
        string = input()
        if ":" in string:
            for i in range(len(string)):
                if string[i] == ':':
                    index = i
            list_of_products.append(string[:index])
            list_of_names.append(string[(index+2):])
        else:
            return list_of_products, list_of_names, string

def printInvertSortedList(characters_products_bag):    
    characters_products_bag = sorted(characters_products_bag, reverse = True)
    for product in characters_products_bag:
        print(product)

def whatProductCarryCharacter():
    index = 0
    characters_products_bag = []
    list_of_products, list_of_names, name = createListOfProduct()
    for i in range(len(list_of_names)):
        if list_of_names[i] == name:
            characters_products_bag.append(list_of_products[i])
    printInvertSortedList(characters_products_bag)


whatProductCarryCharacter()
