n=10
list1=[]
start=0

for i in range(n): #сделали поле из 30 000 ячеек с нулями
    list1.append(0)

stroka=tuple(input()) #разбили строку со знаками, создали кортеж действий

for j in range(len(stroka)):
    if stroka[j]=='>':
        start=start+1
        if start>=n:
            start=start-n*(start//n)
    elif stroka[j]=='<':
        start=start-1
        if start<0:
                start=n+start
    elif stroka[j]=='+':
        list1[start]=list1[start]+1
        if list1[start]>255:
            list1[start]=list1[start]-256*(list1[start]//256)
    elif stroka[j]=='-':
        list1[start]=list1[start]-1
        if list1[start]<0:
                list1[start]=256+list1[start]
    elif stroka[j]=='.':
        print(list1[start])





