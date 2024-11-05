from operation import a,b
def test_a():
    assert a(9,8) == 1
    assert a(5, 6) == -1

def test_b():
    assert b(9,8) == 72
    assert b(5, 6) == 30
