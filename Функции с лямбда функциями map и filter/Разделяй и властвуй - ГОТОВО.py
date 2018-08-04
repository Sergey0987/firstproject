#Вариант 1 в несколько строк

filtr_delenue_na_9=list(filter(lambda x: x%9 == 0, range(10,100)))

spisok_kvadraty = list(map(lambda x: x*x,filtr_delenue_na_9))

summa_kvadratov = sum(spisok_kvadraty)

print(summa_kvadratov)


#Вариант 2 в одну строку

print(sum(list(map(lambda y: y*y , list(filter(lambda x: x%9 == 0, range(10,100)))))))

