#Напишите и запустите блок кода, посмотрите на результат выполнения программы
x=38


print('дратути!')
if x<0:
    print('Меньше нуля')
print('дотвидания!')
#примеры
a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if a > b and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')
# можно сравнивать
if '34' >  "123": #значения строчных символов, осуществляется по первым двум
    print('успех')
if '123' >  "12": #если первые два значения равны то по "длине строки"
    print('успех')
if [1, 2] > [1, 1]: #можно сравнивать списки
    print('успех')
if {4, 5, 6, 7} >= {4, 5, 6}: #можно сравнивать множества
    print('успех')

# Нельзя сравнивать разные типы данных
#if "6" > 5:
#    print('успех')

#if [5, 6] > 5:
#    print('успех')

# НО
if "6" != 5:
    print('успех')# потому, что разные типы данных не равны