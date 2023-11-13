#in test files have test word in beggining or end (ex: _test or test_)

from app.my_mod import enlarge

def test_example():
    assert 2+2 == 4

def test_enlarge():
    assert enlarge(10) == 10000

#you can now use pytest package to run this test

