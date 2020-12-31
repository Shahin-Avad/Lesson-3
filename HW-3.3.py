def my_func(a, b, c):
     
    num_list = [a, b, c]
    max1_max2 = []
    max1 = max(num_list)
    max1_max2.append(max1)
    num_list.remove(max1)
    max2 = max(num_list)
    max1_max2.append(max2)
    
    return sum(max1_max2)

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))

print(my_func(x, y, z))
