"""
Фильтрация
Напишите функцию filter_list, которая принимает функцию f и список lst.

Функция f обязательно должна проверять определенное условие и возвращать булев тип.

Задача функции filter_list состоит в том, чтобы вернуть новый список,
составленный из элементов входного lst, отфильтрованных согласно функции f.
"""
#
# def filter_list(f, lst: list) -> list:
#     return [i for i in lst if f(i)]

"""
Фильтрация - 2
На основании предыдущей функции filter_list, напишем новую функцию filter_collection. Особенность функции filter_collection заключается в том, что она возвращает тот же тип коллекции, который она принимала на вход. 

А остальной принцип  ее работы похож с функцией filter_list: обе принимают функцию f для проверки, при помощи которой фильтруются элементы коллекции

Функция f обязательно должна проверять определенное условие и возвращать булев тип.
"""

# def filter_collection(f: callable, args):
#     if isinstance(args, str):
#         return ''.join(x for x in args if f(x))
#     return type(args)(x for x in args if f(x))
#
#
#
# def is_positive(num):
#     return num > 0
#
# numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
# positive_numbers = filter_collection(is_positive, numbers)
# print(positive_numbers)


"""
Функция aggregation
Реализуйте функцию aggregation, которая принимает на вход функцию func и коллекцию элементов sequence.

Функция func будет принимать только два элемента.

Задача функции aggregation уметь накапливать результат вычисления функции func путем последовательного применения ее ко всем элементам. Но так как функция func умеет работать только с двумя значениями, вам необходимо передавать элементы последовательно парами. В результате у вас должен получиться список, в котором копятся результаты работы функции aggregation

Пример, в качестве func возьмем функцию 

def get_add(x, y):
    return x + y
Коллекцией у нас будет следующий список

numbers = [5, 2, 4, 3, 5]
Применяя func к первым элементам коллекции 5 и 2, получим сумму 7. Это первое наше агрегированное значение

Далее берем уже накопленное значение 7 и следующий необработанный элемент 4, суммируем и получаем новую агрегацию 11.

Затем суммируем нашу агрегацию 11 со значением 3, получаем 14. И в конце добавляем последний элемент и готово итоговое значение 19. В итоге в процессе применения функции func мы нашли следующие значения [7, 11, 14, 19]. Данный список и нужно будет вернуть в качестве ответа.
"""


def aggregation(func, sequence, initial=None) -> int | float:
    if initial != None:
        sequence.insert(0, initial)
    result: list[int | float] = [func(sequence[0], sequence[1])]
    for i in range(2, len(sequence)):
        result.append(func(sequence[i], result[-1]))
    return result[-1]


print(aggregation(lambda x, y: x * y, [2, 5, 10, 1, 2], initial=50))
