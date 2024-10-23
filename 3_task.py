'''
Джонатану начинает казаться, что Гвидо проникся к нему уважением. По крайней мере, он больше не делает
в его присутствии замечаний по поводу ограниченности человеческого интеллекта.
А однажды даже обратился к программисту за помощью!

Появившееся на экране терминала лицо Гвидо выглядит озабоченным (видимо, он не только обновил
эмоциональную прошивку, но и обновил механику лица, мимика стала гораздо выразительнее). Он говорит:

— У одного из наших автоматов, которые присваивают порядковые имена новым машинам, произошел сбой.
Обычно он формирует имена следующим образом: составляет список всех возможных последовательностей в
алфавитном порядке из пяти букв, используя только символы X, Y и Z.

Но что-то пошло не так, программа именования повреждена! А нам нужно срочно выяснить, какое имя
досталось машине под номером
179
179. Начало списка ты видишь на экране. Найди ответ на заданный вопрос как можно скорее!
Это будет засчитано как прохождение очередного испытания.
'''
# from audioop import reverse
#
#
# def xyzcount(n: int, res='') -> str:
#     xyz = ['X', 'Y', 'Z']
#     if n <= 3:
#         res += xyz[n-1]
#         return res.rjust(5, 'X')
#     res += xyz[n % 3]
#     n = n // 3
#     return xyzcount(n, res)
#
# for i in range(1, 179+1):
#     print(i, xyzcount(i))

def generate_sequences(chars, length):
    if length == 0:
        return ['']
    smaller_sequences = generate_sequences(chars, length - 1)
    sequences = []
    for seq in smaller_sequences:
        for char in chars:
            sequences.append(seq + char)
    return sequences

# Генерируем все возможные последовательности из пяти букв
sequences = generate_sequences(['X', 'Y', 'Z'], 5)

# Сортируем последовательности в алфавитном порядке
sequences.sort()

# Находим 179-ю последовательность (индексация с 0, поэтому 178)
result = sequences[178]

print(f"Имя машины под номером 179: {result}")