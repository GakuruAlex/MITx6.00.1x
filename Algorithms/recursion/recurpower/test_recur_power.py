import pytest
from Algorithms.recursive.recurPower.recurpower.recur_power import recurPower

#Test recurPower with zero as exponent
@pytest.mark.parametrize("base,exp,result",[
    (2,0,1),
    (-2,0,1),
    (10,0,1),
    (-10,0,1)
])
class TestRecurPowerWithZero:
    def test_recur_power_with_zero(self,base,exp,result):
        assert recurPower(base,exp) == result

#Test recurPower with negative base and even exponent
@pytest.mark.parametrize("base, exp, result",[
    (-3,2,9),
    (-3,4, 81),
    (-4,2,16),
    (-5,2,25)
])
class TestRecurPowerWithNegBaseAndEvenExp:
    def test_recur_power_with_negative_base_and_even_exp(self, base, exp, result):
        assert recurPower(base,exp) == result

#Test recursive power with negative base and odd exponent
@pytest.mark.parametrize("base,exp,result",[
    (-3,3,-27),
    (-2,5,-32),
    (-5,3,-125),
    (-4,3,-64),
])
class TestRecurPowerWithNegBaseAndOddExp:
    def test_recur_power_with_negative_base_and_odd_exp(self, base, exp, result):
        assert recurPower(base, exp) == result


#Test power with recursion on base and exponent both positive
@pytest.mark.parametrize("base, exp, result",[
(3,3,27),
(2,5,32),
(5, 3, 125),
(4, 3, 64),
(3,2,9),
(3,4, 81),
(4,2,16),
(5,2,25),
])

class TestRecurPowerWithPosBaseAndExp:
    def test_recur_power_with_positive_base_and_exp(self,base, exp, result):
        assert recurPower(base, exp) == result


@pytest.mark.xfail(reason="This test is supposed to fail!")
def test_recur_power_for_known_failure():
    assert recurPower(2,3) == 4