import urwid

password = input('Введите пароль: ')


def is_very_long(password):
    if len(password) > 12:
        return True


def has_digit(password):
    for i in password:
        if i.isdigit():
            return True


def has_letters(password):
    for i in password:
        if i.isalpha():
            return True


def has_upper_letters(password):
    for i in password:
        if i.isupper():
            return True


def has_lower_letters(password):
    for i in password:
        if i.islower():
            return True


def has_symbols(password):
    for i in password:
        if i in '''.,?!:;'"-_(){}[]/\|<>~`@#$%^&*=+ ''':
            return True


checks = [is_very_long(password), has_digit(password), has_letters(password), has_upper_letters(password),
          has_lower_letters(password), has_symbols(password)]


def check_password(checks):
    score = 0
    for i in checks:
        if i:
            score += 2
    return score


score = check_password(checks)

print("Рейтинг этого пароля:", score)
