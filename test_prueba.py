from prueba import add

def test_addition():
    result = add(2, 4)
    assert result == 6

    result = add(-1, 3)
    assert result == 2

    result = add(0, 0)
    assert result == 0