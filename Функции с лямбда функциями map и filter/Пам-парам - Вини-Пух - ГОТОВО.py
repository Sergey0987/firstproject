def pesnia(song):
    from functools import reduce
    
    song = song.split(' ')
#    print(song)

    list_glasnih = list(map(lambda x: list(filter(lambda y: y == 'а' or y == 'е' or y == 'и' or y == 'о' or y == 'у' or y == 'ы' or y == 'ё' or y == 'э' or y == 'ю' or y == 'я', x)), song))

    len_of_phrase = list(map(lambda x: len(x) , list_glasnih))

    srednee_znachenie = int((reduce(lambda x,y: x + y, len_of_phrase)) / len(len_of_phrase))

    filterNumbers = list(filter(lambda x: x != srednee_znachenie, len_of_phrase))

#    print(filterNumbers)

    if len(filterNumbers) > 0:
        return 'Пам парам' # что-то не так с ритмом
    else:
        return 'Парам пам-пам' # все хорошо с ритмом
    
    
print(pesnia('Пар-пам пам-пам'))
