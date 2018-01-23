from src import diffie_hellman, caesar


def test_naive_modexp():
    assert diffie_hellman.naive_modexp(3, 3, 3) == 0

def test_naive_modexp_1():
    assert diffie_hellman.naive_modexp(4, 13, 497) == 445

def test_naive_modexp_2():
    assert diffie_hellman.naive_modexp(595, 703, 991) == 342    

    
def test_optimized_modexp_0():
    assert diffie_hellman.modexp(3, 3, 3) == 0

def test_optimized_modexp_1():
    assert diffie_hellman.modexp(4, 13, 497) == 445

def test_optimized_modexp_2():
    assert diffie_hellman.modexp(595, 703, 991) == 342    


def test_make_huge_num():
    const_num = 512
    for i in range(5):
        assert len(bin(diffie_hellman.make_huge_num(const_num))) == const_num + 2

        
def test_diffi_hellman():
    alice = diffie_hellman.User()
    bob = diffie_hellman.User()

    alice.calc_private_key(bob.A)
    bob.calc_private_key(alice.A)

    assert alice.private_key == bob.private_key
    
