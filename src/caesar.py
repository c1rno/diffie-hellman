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
    if letter not in ABC:
        return ' '

    x = ABC.index(letter)
    coded_index = (x + key) % len(ABC)
    return ABC[coded_index]


def decode(letter: str, key: int = KEY)-> str:
    if letter not in ABC:
        return ' '

    y = ABC.index(letter)
    decoded_index = (y - key + len(ABC)) % len(ABC)
    return ABC[decoded_index]


def code_word(word: str, key: int = KEY) -> str:
    return ''.join(
        map(
            lambda x: code(x, key),
            word
        )
    )


def decode_word(word: str, key: int = KEY) -> str:
    return ''.join(
        map(
            lambda x: decode(x, key),
            word
        )
    )


if __name__ == '__main__':
    original = 'ПРИВЕТ'
    coded_default_key = code_word(original)
    decoded_default_key = decode_word(coded_default_key)

    coded_2_key = code_word(original, 4)
    decoded_2_key = decode_word(coded_2_key, 4)

    print('''
original = {}
coded(3) = {}
decoded(3) = {}
coded(2) = {}
decoded(2) = {}
    '''.format(
        original,
        coded_default_key,
        decoded_default_key,
        coded_2_key,
        decoded_2_key
    ))

