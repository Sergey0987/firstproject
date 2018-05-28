def WhoAreYouAndHellow():
    ORD_A=ord('А') #1040
    ORD_YA=ord('Я') #1071
    ORD_a=ord('а') #1072
    ORD_ya=ord('я') #1103

    PRODOLJAY_CIKL=0 # при 0 внешний цикл while будет продолжаться
    
    while PRODOLJAY_CIKL==0:

        PRODOLJAY_CIKL=1
    
        name=input('Введите имя: ')

        for i in range(1,len(name)):
            if ord(name[i])<ORD_a or ord(name[i])>ORD_ya:
                PRODOLJAY_CIKL=0
                
        if name.count(' ')!=0 or ORD_A>ord(name[0]) or ord(name[0])>ORD_YA or PRODOLJAY_CIKL==0:
            PRODOLJAY_CIKL=0
        else:
            print('Привет,',name + '!')

WhoAreYouAndHellow()
