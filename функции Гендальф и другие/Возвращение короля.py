def createListOfProduct():
    list_of_products = []
    list_of_names = []
    counter = 0
    while counter != 1:
        string = input()
        if ": " in string:
            for i in range(len(string)):
                if string[i] == ':':
                    index = i
                    list_of_products.append(string[:index])
                    list_of_names.append(string[(index+2):])
        else:
            counter = 1
            return list_of_products, list_of_names


def countNameAsProducts(list_of_names):
    unic_names = []
    count_names = []
    for i in range(len(list_of_names)):
        if list_of_names[i] not in unic_names:
            unic_names.append(list_of_names[i])
            count_names.append(1)
        else:
            count_names[len(count_names)-1] = count_names[len(count_names)-1] + 1

    return unic_names, count_names


def findWhoCarryMaxProducts(unic_names, count_names):
    name_of_character_max_carry = []
    for i in range(len(count_names)):
        if len(name_of_character_max_carry) == 0:
            index = 0
            name_of_character_max_carry.append(unic_names[i])
        else:
            if count_names[index] == count_names[i]:
                name_of_character_max_carry.append(unic_names[i])
            elif count_names[index] < count_names[i]:
                name_of_character_max_carry.clear()
                name_of_character_max_carry.append(unic_names[i])
                index = i
#    print(name_of_character_max_carry)
    return name_of_character_max_carry


def printWhoCarryMaxProducts(name_of_character_max_carry, unic_names, count_names):
    first_alfavit_character = name_of_character_max_carry[0]
    for i in range(len(unic_names)):
        if unic_names[i] == first_alfavit_character:
            print(first_alfavit_character, count_names[i])
            return

def whoCarryMaxProducts():
    index = 0
    list_of_products, list_of_names = createListOfProduct()
    list_of_names = sorted(list_of_names)
    unic_names, count_names = countNameAsProducts(list_of_names)
#    print(unic_names)
#    print(count_names)
    name_of_character_max_carry = findWhoCarryMaxProducts(unic_names, count_names)
    printWhoCarryMaxProducts(name_of_character_max_carry, unic_names, count_names)    


whoCarryMaxProducts()
