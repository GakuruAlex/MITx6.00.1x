import pytest

from is_in import isIn

#Test isIn with empty string
@pytest.mark.parametrize("char, aStr, result",[
    ('a', '', False),
    ('a', " ", False),
])
class TestIsInOnEmptyString:
    def test_is_in_on_empty_string(self, char, aStr, result):
        assert isIn (char, aStr) == result

# Test isIn function with length of string odd
@pytest.mark.parametrize("char, aStr, result",[
    ('q', 'ccdeeijlmoppqqtuuvy', True),
    ('x', 'x', True),
    ('x', 'b', False),
    ('v', 'acdhjlopqsvwy', True),
    ('p', 'acdhrrs', False),
    ('h', 'adiloqqvvyz', False)
])
class TestIsInWithOddLenOfString:
    def test_is_in_odd_len(self, char, aStr, result):
        assert isIn(char, aStr) == result

#Test isIn function with length of string even
@pytest.mark.parametrize("char, aStr, result",[
    ('m', 'fgijnnpptwxxxy', False),
    ('c', 'cffggkssuvxxyz', True),
    ('y', 'korstz', False),
    ('f','cf', True),
])
class TestIsInWithEvenLenOfString:
    def test_is_in_with_even_len(self, char, aStr, result):
        assert isIn(char, aStr) == result

@pytest.mark.xfail(reason="This test is meant to fail")
def test_is_in_for_known_failure():
    assert isIn("x", "abcde") == True