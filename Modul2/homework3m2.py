list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
str_ = ('Я езжу на автомабиле марки ')
for i in (list_):
    print(('Я езжу на автомабиле марки ') +i) # Если не придется менять значение текста можно так
    print((str_) + i) # либо такой вариант, если в дальнейшем понадобится изменить значение str_

cars_count = input("Введите количество автомобилей в Вашем гараже : " )
s = int(cars_count)
for j in range(0,11,2): #в цикле из шага номер 2 увеличение переменной на 10 в каждом шаге цикла
    print("Ваш парк через месяц :", j+(s+10))



