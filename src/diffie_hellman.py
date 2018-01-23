from .common import *


class User(object):
    g = make_huge_num(512)
    p = make_huge_num(16)
    
    def __init__(self):
        self.a = make_huge_num(1024)
        self.A = modexp(self.g, self.a, self.p)
        self.private_key = 0

    def calc_private_key(self, other_public_key):
        self.private_key = modexp(other_public_key, self.a, self.p)

    def __str__(self):
        return 'a = {}\nA = {}\nprivate = {}'.format(self.a, self.A, self.private_key)

   
if __name__ == '__main__':
    alice = User()
    bob = User()

    alice.calc_private_key(bob.A)
    bob.calc_private_key(alice.A)

    print('Alice', alice)
    print('Bob', bob)
    
