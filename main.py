# В кортеж список нельзя ни добавить, ни удалить. Но если его элемент список,
# то в этот список можно добавить/ удалить

# a = (1, ["one", "two"])
# b = () #пустой кортеж
# c = tuple() # с помощью готовой функции
# d = tuple('Hello guy') # разбивает строку побуквенно
# a[1][0] = 3

a = (1, 2, 3, "poo", [1, 5, 6], True) #!!!!кортеж меньше весит
b = [1, 2, 3, "poo", [1, 5, 6], True]

#a.count(2)  # выводит кол-во раз сколько встречвается значение в кортеже
#index = a.index("poo") # работает с числами, строками - выводит порядковый номер

# size_a= a.__sizeof__()
# size_b= b.__sizeof__()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    number = 100 #integer
    boolean_value = True #=> 1
    another_value = False #=> 0
    float_number = 100.5 #float
    text = 'Цитата: \'программирование\''

    list1 = {0: 25, "name": "Anna"}
    list2 = {"car": "машина", "table": "стол"}

    print(list2["table"])

# print(3 in a) # наличие элемента в кортеже/ списке
# print(0 not in a)

numbers = (1, 2, 3, 2, 1, 2)
print(numbers.count(2)) # 3 (число 2 встречается три раза)
print(numbers.index(3)) # 2 (индекс первого вхождения 3)
