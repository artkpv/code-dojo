#! python3

"""
https://contest.yandex.com/algorithm2016/contest/2497/problems/
Буквы адреса

Ограничение времени	1 секунда
Ограничение памяти	512Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Байтазар хочет завести себе Яндекс.Почту. Однако выбранное им имя, составленное из строчных английских букв, уже кем-то используется. Тогда Байтазар решил составить новое имя следующим способом. Сначала он строит слово V, читая первоначально выбранное имя слева направо и выписывая все гласные в порядке их появления. Затем он аналогичным образом строит слово C из согласных. Байтазар считает гласными буквы «a», «e», «i», «o», «u», а также букву «y», а все остальные буквы считает согласными. Новым именем Байтазара будет либо слово V, либо слово C.
Чтобы окончательно выбрать между двумя вариантами, Байтазар хочет узнать, какой из них является лексикографически наибольшим. Напомним, что для того, чтобы сравнить два слова лексикографически, нужно найти самую левую позицию, на которой символы в этих словах различаются, после чего сравнить эти символы. То слово, у которого символ на соответствующей позиции идёт в алфавите позже, лексикографически больше. Если такой позиции нет, больше то слово, длина которого больше.
Формат ввода

Входные данные — непустая строка T, состоящая из строчных английских букв. Длина строки не превосходит 106 букв.
Формат вывода

Если слово, составленное из гласных, лексикографически больше, выведите «Vowel». В противном случае выведите «Consonant».
Пример 1

Ввод	Вывод
consonant
Vowel
Пример 2

Ввод	Вывод
vowel
Consonant
"""

S = input().strip()

v, c = None, None
for i in range(len(S)):
    if S[i] in 'bcdfghjklmnpqrstvwxz' and c is None:
        c = S[i]
    elif S[i] in 'aeiouy' and v is None:
        v = S[i]

    if c is not None and v is not None:
        print('Consonant' if c > v else 'Vowel')
        exit()

if v is not None:
    print('Vowel')
elif c is not None:
    print('Consonant')

