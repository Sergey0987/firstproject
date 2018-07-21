def translateLenNumber1(number, string, list_from_0_to_9):
    if len(str(number)) == 1:
        for i in range(len(list_from_0_to_9)):
            if i == number:
                string = list_from_0_to_9[i]
                return string

def translateLenNumber2(number, string, list_from_0_to_9, list_from_10_to_19, list_from_20_to_90):
        if number < 20 and number > 9:
            for i in range(len(list_from_10_to_19)):
                if i == number%10:
                    print(list_from_10_to_19[i])
        elif number >= 20 and number <= 99:
            for i in range(len(list_from_20_to_90)):
                if i == number//10 - 2:
                    string = string + list_from_20_to_90[i] + ' '
            for i in range(len(list_from_0_to_9)):
                if i == number%10:
                    string = string + list_from_0_to_9[i]
            return string    

def translateLenNumber3(number, string, name_of_100, list_from_0_to_9, list_from_10_to_19, list_from_20_to_90):
        for i in range(len(list_from_0_to_9)):
            if number//100 == i:
                string = string + list_from_0_to_9[i] + ' ' + name_of_100 + ' and '
        if number%100 >= 10 and number%100 <= 19:
            for i in range(len(list_from_10_to_19)):
                if i == number%10:
                    string = string + list_from_10_to_19[i]
        elif number%100 >= 20 and number%100 <= 99:
            for i in range(len(list_from_20_to_90)):
                if i == number%100//10 - 2:
                    string = string + list_from_20_to_90[i] + ' '
            for i in range(len(list_from_0_to_9)):
                if i == (number - (number - number%100))%10:
                    string = string + list_from_0_to_9[i]        
        return string

def sayItAsWords(number):
    list_from_0_to_9 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    list_from_10_to_19 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eigthteen', 'nineteen']
    list_from_20_to_90 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    name_of_100 = 'hundred'
    string = ''
    if len(str(number)) == 1:
        string = translateLenNumber1(number, string, list_from_0_to_9)
        print(string)
        return
    elif len(str(number)) == 2:
        string = translateLenNumber2(number, string, list_from_0_to_9, list_from_10_to_19, list_from_20_to_90)
        print(string)
        return
    elif len(str(number)) == 3:
        string = translateLenNumber3(number, string, name_of_100, list_from_0_to_9, list_from_10_to_19, list_from_20_to_90)
        print(string)
        return
        
sayItAsWords(195)
