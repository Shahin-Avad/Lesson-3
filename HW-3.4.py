a = float(input("Введите число, которое хотите возвести в степень: "))
b = float(input("Введите степень, в которую хотите возвести число: "))


def my_func_1(x, y):
    return x ** y

def my_func_2(x, y):
    i = 1 # текущая степень
    result = 1
    while i <= b:
        result *= a
        i += 1
    return result

print("Сетпень через '**': ", (my_func_1(a, b)))   

print("Сетпень через цикл: ", my_func_2(a, b))
