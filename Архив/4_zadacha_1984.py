n=int(input('Число комманд от правительства = '))
voyna='Евразия'
mir='Остазия'
list1=[]
for i in range(n):
    a=input()
    if a=='С кем война?':
        list1.append(voyna)
    elif a=='С кем мир?':
        list1.append(mir)
    else:
        voyna,mir=mir,voyna
for j in list1:
    print(j)
