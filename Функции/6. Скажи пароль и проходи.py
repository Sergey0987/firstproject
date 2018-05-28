def askPassword():
    TRUE_PASSWORD = 'password'
    attempt_counter = 0
    number_of_attempt = 3
    for i in range(number_of_attempt):
        input_password = input('Введите пароль:')
        if input_password == TRUE_PASSWORD:
            print('Пароль принят')
            break
        else:       
            attempt_counter = attempt_counter + 1
            print('Пароль неверный. Осталось',number_of_attempt - attempt_counter,'попытки')
            if attempt_counter == 3:
                print('В доступе отказано')
        
    
askPassword()
