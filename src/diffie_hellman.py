import random


def naive_modexp(base: int, degree: int, modulus: int) -> int:
    return base ** degree % modulus


def modexp(base, degree, modulus):
    _degree  = bin(degree)[2:]
    _base = base
    r = 1

    for val in _degree[::-1]:
        r = (r * _base ** int(val)) % modulus
        _base = (_base ** 2) % modulus

    return r


def make_huge_num(bytes_num: int = 1024) -> int:
    min_val = int('1{}'.format(''.join('0' for x in range(bytes_num - 1))), 2)
    max_val = int(''.join('1' for x in range(bytes_num)), 2)
    return random.randrange(int(min_val), int(max_val))


class User(object):
    g = make_huge_num(512)
    p = make_huge_num(16)
    
    def __init__(self):
        self.a = make_huge_num(1024)
        self.A = modexp(self.g, self.a, self.p)
        self.secret = None

    def calc_secret(self, other_A):
        self.secret = modexp(other_A, self.a, self.p)

    def __str__(self):
        return '''g = {}
p = {}
a = {}
A = {}
secret = {}'''.format(self.g, self.p, self.a, self.A, self.secret)

   
if __name__ == '__main__':
    alice = User()
    bob = User()

    alice.calc_secret(bob.A)
    bob.calc_secret(alice.A)

    print('''
Alice:
{}

Bob:
{}
'''.format(alice, bob))
    
