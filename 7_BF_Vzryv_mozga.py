n=10
list1=[]
list2=[]
start=0

for i in range(n): #сделали поле из 30 000 ячеек с нулями
    list1.append(0)

stroka=input() #разбили строку со знаками познаково и добавили в список
for i in stroka:
    list2.append(i)
list2=tuple(list2) #защита, чтобы случайно не нарушит последовательность комманд

for j in range(len(list2)):
    if list2[j]=='>':
        start=start+1
        if start>=n:
            start=start-n*(start//n)
    elif list2[j]=='<':
        start=start-1
        if start<0:
                start=n+start
    elif list2[j]=='+':
        list1[start]=list1[start]+1
        if list1[start]>255:
            list1[start]=list1[start]-256*(list1[start]//256)
    elif list2[j]=='-':
        list1[start]=list1[start]-1
        if list1[start]<0:
                list1[start]=256+list1[start]
    elif list2[j]=='.':
        print(list1[start])





