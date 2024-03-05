from collections import namedtuple

Kitob = namedtuple('Kitob', ['kitob', 'yozuvchi'])

kitoblar = [
    Kitob(kitob='Matnlar va tafsilotlar', muallif='Ali Navruzov'),
    Kitob(kitob='Python dasturlash tilida algoritmlar', muallif='John Smith'),
    Kitob(kitob='Maftuning Qutulishi', muallif='Abdulla Qodiriy')
]

for kitob in kitoblar:
    print(f"kitob: {kitob.kitob}, muallif: {kitob.muallif}")
