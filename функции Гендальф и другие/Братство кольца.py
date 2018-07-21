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

def whoCarryProduct():
    index = 0
    list_of_products, list_of_names, product = createListOfProduct()
    for i in range(len(list_of_products)):
        if list_of_products[i] == product:
            print(list_of_names[i])
            return


whoCarryProduct()
