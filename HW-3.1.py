def div(x,y):
    
    while y == 0:
        y = float(input("Введите число неравное нулю: ", ))
        
    print("Результат деления равен: ")
    return round(x / y, 2)

a = float(input("введите чеслитель: "))
b = float(input("введите значенатель: "))

print(div(a,b))
