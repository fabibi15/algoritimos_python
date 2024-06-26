from scripts.fibonacci import fibonacci

def test_firts_10_numbers():
    res = fibonacci(10)
    assert res == [0,1,1,2,3,5,8,13,21,34]