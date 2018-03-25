a=('Щи', "Борщ", "Щавелевый суп", "Овсяный суп", "Суп по-чабански")
n=int(input())
if n>len(a):
    for i in a:
        print(i)
    for i in range(n-len(a)):
        print(a[i])
else:
    for i in range(n):
        print(a[i])


