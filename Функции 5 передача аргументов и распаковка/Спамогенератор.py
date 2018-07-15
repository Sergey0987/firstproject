def spamogenerator(name, date_of_meeting, e_mail_of_recipient, place_of_meeting = 'Moscow'):
    template = [('To:' + e_mail_of_recipient), ('Здравствуйте, ' + name + '!'), ('Были бы рады видеть вас на встрече начинающих программистов в ' + place_of_meeting + ', которая пройдет ' + date_of_meeting + '.')]
    print(*template, sep = '\n')
    print()

spamogenerator('Maria', '26.07.2018', 'maria@yandex.ru')
spamogenerator('Ivan', '24.05.2018', 'ivan@mail.ru', 'Санкт-Петербург')
