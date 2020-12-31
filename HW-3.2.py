def f_dict(a, b, c, d, e, f):
    return ' '.join([a, b, c, d, e, f])

name = input("Введите имя: ")
lastname = input("Введите вашу фамилию: ")
year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
e_mail = input("Ввеите ваш E-mail: ")
tel = input("Введите ваш номер телефона: ")

print(f_dict(name, lastname, year, city, e_mail, tel))
