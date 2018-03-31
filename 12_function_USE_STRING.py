def useString(a,s):
    a=[int(i) for i in a.split()]
    s=s.split()
    b=0
    s[0]=s[0].replace(s[0][0],chr(ord(s[0][0])+32),1)
    for j in range(len(a)):
        if b==0:
            b=s[a[j]-1]
            if ord(b[0][0])>1072 or ord(b[0][0])<1040:
                b=b.replace(b[0][0],chr(ord(b[0][0])-32),1)
        else:
            b=b+' '+s[a[j]-1]
    
    return b

print(useString(input('Введите номера слов: '),input('Введите строку: ')))
