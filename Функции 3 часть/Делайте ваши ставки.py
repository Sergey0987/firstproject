def doBet(horse_number, bet):
    global dictOfHorses
    if bet <= 0 or dictOfHorses[str(horse_number)] != 'free':
        print('Что-то пошло не так. Попробуйте еще раз')
    else:
        dictOfHorses[str(horse_number)] = bet
        print('Ваша ставка в размере ' + str(bet) + ' на лошадь ' + str(horse_number) + ' принята!')


volume_of_horses=10
key_list=[]
value_list=[]

for i in range(1,volume_of_horses+1):
    key_list.append(str(i))

for i in range(1,volume_of_horses+1):
    value_list.append('free')

dictOfHorses = dict(zip(key_list, value_list))
doBet(1, 10)
doBet(1, 100)
doBet(2, 0)
doBet(2, 200)

    
