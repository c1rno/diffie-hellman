from .common import *

ABC = [
    'А',
    'Б',
    'В',
    'Г',
    'Д',
    'Е',
    'Ё',
    'Ж'
    'З',
    'И',
    'Й',
    'К',
    'Л',
    'М',
    'Н',
    'О',
    'П',
    'Р',
    'С',
    'Т',
    'У',
    'Ф',
    'Х',
    'Ц',
    'Ч',
    'Ш',
    'Щ',
    'Ъ',
    'Ы',
    'Ь',
    'Э',
    'Ю',
    'Я'
]

codedABC = [
    'Г',
    'Д',
    'Е',
    'Ё',
    'Ж',
    'З',
    'И',
    'Й',
    'К',
    'Л',
    'М',
    'Н',
    'О',
    'П',
    'Р',
    'С',
    'Т',
    'У',
    'Ф',
    'Х',
    'Ц',
    'Ч',
    'Ш',
    'Щ',
    'Ъ',
    'Ы',
    'Ь',
    'Э',
    'Ю',
    'Я',
    'А',
    'Б',
    'В'
]

KEY = 3


def code(letter: str, key : int = KEY) -> str:
    x = ABC.index(letter)
    coded_index = (x + key) % len(ABC)
    return ABC[coded_index]


def decode(letter: str, key: int = KEY)-> str:
    y = ABC.index(letter)
    decoded_index = (y - key + len(ABC)) % len(ABC)
    return ABC[decoded_index]


if __name__ == '__main__':
    original = 'ПРИВЕТ'
    decoded = 'ТУЛЕИХ'

    tmp = []
    
    for letter in original:
        tmp.append(code(letter))

    print(''.join(tmp))

    tmp = []
    
    for letter in decoded:
        tmp.append(decode(letter))

    print(''.join(tmp))
    
