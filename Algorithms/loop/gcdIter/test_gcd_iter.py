import pytest
from gcd_iter import gcdIter
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
    def test_gcd_ite(self, a, b, result):
        assert gcdIter(a, b) == result