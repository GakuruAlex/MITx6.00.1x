import pytest
from gcd_recur import gcdRecur
@pytest.mark.parametrize("a, b, result",[
    (2,12,2),
    (6,12,6),
    (9,12,3),
    (17,12,1),
    (1,12,1),
    (-4,12,4),
    (-6,12,6),
])
class TestGcdIte:
    def test_gcd_iter(self, a, b, result):
        assert gcdRecur(a, b) == result