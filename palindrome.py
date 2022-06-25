# assert - zwraca ?
# dir ("")
# dir([]) wyswietla metody listy
# help(help)
# isalnum sprawdz4e czy cos jest alfa numereyczne
# %%writefile lib %readfile
# z jednym % dzialaja w jednej lini,  z dwoma procentami dziala w jednym obiekcie(?)
# timeit y = [x for x in range]
# restart and run sal ?
#plik -> 01.notatki.ipynb , palindrome.py,  hello world
# gwiazdka świdczy o tym że plik jest w trakci8e działania
# except i finally (w trakcie jak coś trwa)
# yield
### operatory (np. +, -, /)
# + - konkatenacja , złączenie
# % s - string, %d - też formatowanie
#git - repozytorium (na kompie jest jedno) commit - rewizja - migawka kodu w czasie - zapisywama jakos diff
#brnach - rozgałęienia kodu
# kluczowe instrukcje:
# git init - inicjucje puste repozytorim
# git status - pokazuje aktualny status   (gitignore)
# zmiany do złożenia (na zielono)
# vim , sul - edytor
# _pycache_)
#.ipybn_cheese

# kropka oznacza ze prywatne?

# notepad .gitignore w macu
# nano .gitignore w macu

# rmdir .git (usuwanie katalogu?)

#.ipynb_checkpoint
#.idea
#__pycache__


# nano
# ctrl x
# nano .gitignore
# .idea
# __pycache__
# ctrl o (enter)
# ctrl x    na macu
#
# git status ?


print(y)
def is_palindrom(text: str) -> bool:
    tmp = ""
    for sign in text.lower():
        if sign.isalnum():
            tmp += sign
        if tmp == tmp[::-1]:
            return True
        else:
            return False

    return tmp ==tmp[::-1]

assert is_palindrom("kajak") is True
assert is_palindrom("Kobyła ma mały bok!") is True
assert is_palindrom("dom") is False

    overwriting palindrome.py

    # if text is_palindrome
#
# def one23()
# yield 1
# yield 2
# yield 3
# gen = gen = one23()
#
# lista = [1244]
#
# for el in lista: print(el)
# 1
# 2
# 3
# for el in gem: print(el)
# 1
# 2
# 3
# range(10)
# raange(0, 10)
# y =False
#
# id(x), id(y), is(z)
# 43348680,

z = "adas"
id(z)
x = "adas" xxx xxx"
y=x
id(x), id(y), id(z)
(32134443283, 09812374568, 903838211)
x is y
True
x is z
Flase


Napis = str
help(str)
''
("123asas", "123asas")
"0" + "1"
"01"

"a = $s, %d" (10,20)
"a = 10, 39"

"{a} {b}".format(a=10, b=20)
"10, 20"

"{:^30} {:<6.2f}". format("a", 10)
"             a               10.0"


f"""
{a}
{b}
"""
a
10



