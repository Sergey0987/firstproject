def WhoAreYouAndHellow():
    ORD_A=ord('А') #1040
    ORD_YA=ord('Я') #1071
    ORD_a=ord('а') #1072
    ORD_ya=ord('я') #1103

    name=input('Введите имя: ')

    for i in range(1,len(name)):
        if ord(name[i])<ORD_a or ord(name[i])>ORD_ya:
            return WhoAreYouAndHellow()

    if name.count(' ')!=0 or ORD_A>ord(name[0]) or ord(name[0])>ORD_YA:
        return WhoAreYouAndHellow()
    else:
        print('Привет,',name + '!')

WhoAreYouAndHellow()
