def main():    
    global list_from_string
    global stek
    list_from_string = input().split()
    stek = []
    fromStrToInt(list_from_string)
    reversePolishNotation(list_from_string)
    print(stek[0]) 

def fromStrToInt(argument):
    global list_from_string
    for i in range(len(list_from_string)):
        try:
            list_from_string[i] = int(list_from_string[i])
        except ValueError:
            list_from_string[i] = list_from_string[i]

def reversePolishNotation(argument1):
    result = 0
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
   
main()
