

# Практическое задание по теме: "Словари и множества"

# Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
#
# Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.

my_dict = {'Alex': 1975, 'Nataly': 1978, 'Katy': 2008}
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict.get('Tatyana'))
my_dict.update({'Tatyana': 1955, 'Vladimir': 1947})
del my_dict["Alex"]
print('Операция print(my_dict['"Alex"'] невозможна, т. к. объект удален')
print(my_dict)

my_set = {'Alex', 1975, 'Nataly', 1978, 'Katy', 2008, 'Alex', 1975, 'Nataly', 1978, 'Katy', 2008}
print(my_set)
my_set.update({'Tatyana', 1955})
my_set.remove('Alex')
print(my_set)
