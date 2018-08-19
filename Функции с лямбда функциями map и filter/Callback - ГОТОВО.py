def main():
    askPassword(success, failure)

def fromBifLettersToSmall(login, password):
    login_new = ''
    password_new = ''
    delta_big_and_small_letters = 32
    for i in login:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            login_new = login_new + chr(ord(i) + 32)
        else:
            login_new = login_new + i

    for i in password:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            password_new = password_new + chr(ord(i) + 32)
        else:
            password_new = password_new + i    
    return login_new, password_new
    

def success(login):
    print('Привет, ' + login + '!')

def failure(login, msg_about_failure):
    print('Кто-то пытался притвориться пользователем ' + login + ', но в пароле допустил ошибку: ' + msg_about_failure)

def countVowelLettersInPassword (password, vowel_letters):
    zero_is_our_letter = list(map(lambda letter: list(map(lambda x,y: ord(x) - ord(y) , letter*len(vowel_letters), vowel_letters)), password))
    count_letters_as_zero = len(list(filter(lambda x: 0 in x, zero_is_our_letter)))
    return count_letters_as_zero

def verifyConsonantLettersAndSequence(login, password):
    from functools import reduce
    login_consonant_letter = list(filter(lambda letter: ord('a') <= ord(letter) and ord(letter) <= ord('z')
                                         and letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u' and letter != 'y', login))
    summ_login_consonant_letter = reduce(lambda x,y: x + y, login_consonant_letter)
    
    password_consonant_letter = list(filter(lambda letter: ord('a') <= ord(letter) and ord(letter) <= ord('z')
                                            and letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u' and letter != 'y', password))
    summ_password_consonants_letter = reduce(lambda x,y: x + y, password_consonant_letter)

    if summ_login_consonant_letter == summ_password_consonants_letter:
        return True
    else:
        return False


def askPassword(success, failure):
    login = input()
    password = input()

    login, password = fromBifLettersToSmall(login, password)
    
    vowel_letters = ['a', 'e', 'i', 'o', 'u', 'y']
    msg_wrong_number_of_vowels = 'WRONG NUMBER OF VOWELS' #при возникновении такой ошибки будем прибавлять к сумме ошибок 1
    msg_wrong_consonantes = 'WRONG CONSONANTS' #при возникновении такой ошибки будем прибавлять к сумме ошибок 2
    msg_everything_is_wrong = 'EVERYTHING IS WRONG' #Если сумма ошибок будет 3, выводить эту ошибку
    summ_of_failure = 0
    
    numbers_of_vowel_letters = countVowelLettersInPassword(password, vowel_letters)
    if numbers_of_vowel_letters != 3:
        summ_of_failure = summ_of_failure + 1

    verifi_consonants = verifyConsonantLettersAndSequence(login, password)
    if verifi_consonants == False:
        summ_of_failure = summ_of_failure + 2

    if summ_of_failure == 0:
        success(login)
        return
    elif summ_of_failure == 1:
        failure(login, msg_wrong_number_of_vowels)
        return
    elif summ_of_failure == 2:
        failure(login, msg_wrong_consonantes)
        return
    else:
        failure(login, msg_everything_is_wrong)
        return
        


main()
