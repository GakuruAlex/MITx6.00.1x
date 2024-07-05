import pytest
from grader import polysum
@pytest.mark.parametrize("n, s, result",[
    (51, 47, 6202251.5755),
    (11, 50, 325914.0998),
    (87, 40, 13073696.096),
    (83, 60, 26773010.5575),
    (44, 54, 6093857.0814),
    (79, 73, 35903504.2705),
    (1, 96, -1.881358773488106e+19),
    (41, 50, 4536269.5694),
])
class TestGrader:
    def test_grader(self, n, s, result):
        assert polysum(n, s) == result