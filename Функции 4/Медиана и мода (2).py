def OPN():
    list_from_string = input().split()
    stek = []
    result = 0
    for i in range(len(list_from_string)):
        try:
            list_from_string[i] = int(list_from_string[i])
        except ValueError:
            list_from_string[i] = list_from_string[i]

    for i in range(len(list_from_string)):
        if list_from_string[i] == '*':
            index=len(stek)-2
            result = stek.pop(len(stek)-2) * stek.pop(len(stek)-1)
            stek.insert(index, result)
        elif list_from_string[i] == '/':
            index=len(stek)-2
            result = stek.pop(len(stek)-2) / stek.pop(len(stek)-1)
            stek.insert(index, result)
        elif list_from_string[i] == '+':
            index=len(stek)-2
            result = stek.pop(len(stek)-2) + stek.pop(len(stek)-1)
            stek.insert(index, result)
        elif list_from_string[i] == '-':
            index=len(stek)-2
            result = stek.pop(len(stek)-2) - stek.pop(len(stek)-1)
            stek.insert(index, result)
        else:
            stek.append(list_from_string[i])
    print(stek[0])

OPN()
