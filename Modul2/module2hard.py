# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20)
# программа выдавала нужный пароль result, для одного введённого числа.
# Во вторую вставку нужно написать те пары чисел друг за другом,
# чтобы число из первой вставки было кратно сумме их значений.
# УСЛОВИЯ:
# Первое число не входит в одно из чисел пары
# Пары чисел подбираются от 1 до 20 для текущего числа.
import random
my_list = list(range(21)) #создаем список от 0 до 20
list1 = my_list[1:] # из него берем список чмсел для первых значений пары
list2 = my_list[1:] # и список для вторых значений пары
list3 = my_list[3:] # создаем список для генерации случайных чисел от 3 до 20 (первый камень у ловушки)
n = random.choice(list3) # и переменную "n" из этого списка
print('На первом камне выпало число : ', n)
#def sum_result(): # создаем функцию, для сбора результата
itog = [] # и пустой список для сбора значений полученнных при расчете пар
for i in list1: # задаем цикл по числам от 1 до 20 для первых значений пар
    for j in list2: # и цикл по числам от 1 до 20 для вторых значений пар
        if j != n: #задаем условие, что первое число (n) не должно входить в список вторых значений пар
            if n % (i + j) == 0: #а так же условие, что первое число, - кратно сумме чисел в парах
                itog.append(i) #так как все условия выполнены добавляем по очереди значения пар
                itog.append(j)

result = [] #создаем открытый список для конечного результата т.к. конечный результат должен быть строкой
for k in itog:
    c = str(k) # переводим числовые значения в строчные
    result.append(c)
print("для побега введите : ", ''.join(result))
comments = ("Пожалуйста не удивляйтесь, что мой результат не совпадает с паролем для сверки."
            "Ниже приведен вариант решения задачи в результате которого получены данные пароли."
            "Но хочу отметить, что при таком алгоритме не выолнено следующее условие:"
            "- Пары чисел подбираются от 1 до 20 для текущего числа;"
            "в результате чего теряется как минимум одна пара из едениц для четных первых чисел"
            "так же не учитывается обратная последовательность цикла (без учета в нем значения текущего числа)"
            "что не логично при создании данного пароля. Например значение пары 1 и 3 кратно 8 но ведь 3 и 1 так же "
            "кратно 8, при этом в конечный пароль не попадает. К тому же результат является строкой в которой "
            "обсуждаемые пары принимают значение 13 и 31")
print(comments)

# Второй Вариант решения (Точнее код в результате которого получен список паролей для сверки).
#def generate_password(n):
 #   result = ""  # Инициализируем пустую строку для хранения пароля
  #  for i in range(1, n):  # Цикл по всем числам от 1 до n-1
   #     for j in range(i + 1, n + 1):  # Цикл по числам от i+1 до n
    #        if n % (i + j) == 0:  # Проверяем, кратна ли сумма чисел n
     #           result += str(i) + str(j)  # Добавляем пару чисел к паролю
    #return result


# Пример использования
#for n in range(3, 21):
    #password = generate_password(n)
    #print(f"Пароль для числа {n}: {password}")