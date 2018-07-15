#Шифр Цезаря

def encryptCaesar(msg, shift = 3):
    shift = shift % 33
    msg_encrypt = ''
    for symbol in msg:
        if ord(symbol) >= ord('А') and ord(symbol) <= ord('Я'):
            if ord('Я') - ord(symbol) < shift:
                delta_Ya_Symb = ord('Я') - ord(symbol) + 1
                shift_new = shift - delta_Ya_Symb
                symbol = chr(ord('А') + shift_new)
                msg_encrypt = msg_encrypt + symbol
            else:
                symbol = chr(ord(symbol) + shift)
                msg_encrypt = msg_encrypt + symbol
        elif ord(symbol) >= ord('а') and ord(symbol) <= ord('я'):
            if ord('я') - ord(symbol) < shift:
                delta_Ya_Symb = ord('я') - ord(symbol) + 1
                shift_new = shift - delta_Ya_Symb
                symbol = chr(ord('а') + shift_new)
                msg_encrypt = msg_encrypt + symbol
            else:
                symbol = chr(ord(symbol) + shift)
                msg_encrypt = msg_encrypt + symbol
        else:
            msg_encrypt = msg_encrypt + symbol
    return msg_encrypt
    


def decryptCaesar(msg, shift = 3):
    shift = shift % 33
    msg_decrypt = ''
    for symbol in msg:
        if ord(symbol) >= ord('А') and ord(symbol) <= ord('Я'):
            if ord(symbol) - shift < ord('А'):
                delta_A_Symb = ord(symbol) - ord('А') + 1
                shift_new = shift - delta_A_Symb
                symbol = chr(ord('Я') - shift_new)
                msg_decrypt = msg_decrypt + symbol
            else:
                symbol = chr(ord(symbol) - shift)
                msg_decrypt = msg_decrypt + symbol
        elif ord(symbol) >= ord('а') and ord(symbol) <= ord('я'):
            if ord(symbol) - shift < ord('а'):
                delta_A_Symb = ord(symbol) - ord('а') + 1
                shift_new = shift - delta_A_Symb
                symbol = chr(ord('я') - shift_new)
                msg_decrypt = msg_decrypt + symbol
            else:
                symbol = chr(ord(symbol) - shift)
                msg_decrypt = msg_decrypt + symbol
        else:
            msg_decrypt = msg_decrypt + symbol
    return msg_decrypt
        

#Зашифрока и рашифровка 'АБВабв'
print(encryptCaesar('АБВабв'))
print(decryptCaesar('ГДЕгде'))

#Зашифровка и расшифровка 'ЭЮЯэюя'
print(encryptCaesar('ЭЮЯэюя', shift = 100)) # 100%33 = 1 свдиг будет на 1 символ
print(decryptCaesar('ЮЯАюяа', shift = 100))

