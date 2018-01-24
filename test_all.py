from src import diffie_hellman, caesar


def test_code():
    assert caesar.code('А') == 'Г'

    
def test_decode():
    assert caesar.decode('Г') == 'А'


def test_code_word():
    assert caesar.code_word('ПРИВЕТ') == 'ТУЛЕИХ'

    
def test_fail_code_word():
    assert caesar.code_word('ПРИВЕТ') != 'ПУЛЕИХ'

    
def test_decode_word():
    assert caesar.decode_word('ТУЛЕИХ') == 'ПРИВЕТ'


def test_fail_decode_word():
    assert caesar.decode_word('ПУЛЕИХ') != 'ПРИВЕТ'


def test_code_with_different_keys():
    assert caesar.code_word('ПРИВЕТ', 2) != caesar.code_word('ПРИВЕТ', 3)


def test_decode_with_different_keys():
    assert caesar.decode_word('ТУЛЕИХ', 2) != caesar.decode_word('ТУЛЕИХ', 3)


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

    alice.calc_secret(bob.A)
    bob.calc_secret(alice.A)

    assert alice.p == bob.p
    assert alice.g == bob.g
    assert alice.secret == bob.secret
    assert alice.a != bob.a
    assert alice.A != bob.A
    
