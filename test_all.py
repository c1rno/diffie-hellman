from src import main


def test_naive_modexp():
    assert main.naive_modexp(3, 3, 3) == 0

def test_naive_modexp_1():
    assert main.naive_modexp(4, 13, 497) == 445

def test_naive_modexp_2():
    assert main.naive_modexp(595, 703, 991) == 342    

    
def test_optimized_modexp_0():
    assert main.modexp(3, 3, 3) == 0

def test_optimized_modexp_1():
    assert main.modexp(4, 13, 497) == 445

def test_optimized_modexp_2():
    assert main.modexp(595, 703, 991) == 342    


def test_make_huge_num():
    const_num = 512
    for i in range(5):
        assert len(bin(main.make_huge_num(const_num))) == const_num + 2

        
def test_diffi_hellman():
    alice = main.User()
    bob = main.User()

    alice.calc_private_key(bob.A)
    bob.calc_private_key(alice.A)

    assert alice.private_key == bob.private_key
    
