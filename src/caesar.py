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

KEY = 3


def code(letter: str, key : int = KEY) -> str:
    x = ABC.index(letter)
    coded_index = (x + key) % len(ABC)
    return ABC[coded_index]


def decode(letter: str, key: int = KEY)-> str:
    y = ABC.index(letter)
    decoded_index = (y - key + len(ABC)) % len(ABC)
    return ABC[decoded_index]


def code_word(word: str) -> str:
    return ''.join(
        map(
            code,
            word
        )
    )


def decode_word(word: str) -> str:
    return ''.join(
        map(
            decode,
            word
        )
    )


if __name__ == '__main__':
    original = 'ПРИВЕТ'
    coded = code_word(original)
    decoded = decode_word(coded)

    print('''
original = {}
coded = {}
decoded = {}
    '''.format(original, coded, decoded))

