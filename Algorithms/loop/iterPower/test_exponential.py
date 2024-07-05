import pytest

from exponential import iterPower
#Test  with zero as exponential
@pytest.mark.parametrize("pos_base,zero_exp,zeros_result", [
    (2,0,1),
    (-3,0,1),
    (10,0,1),
    (-10,0,1)
])
class TestIterPowerWithExpoAsZero:
    def test_iterPower_with_zero_as_expo(self,pos_base, zero_exp, zeros_result):
        assert iterPower(pos_base, zero_exp) == zeros_result

#Test with base and exponential as positive values
@pytest.mark.parametrize("base,exp,result", [
    (2,3,8),
    (3,3,27),
    (4,2,16),
])

class TestIterPowerWithPositiveValues:
    def test_iterPower_with_positive_base_and_exp(self,base,exp,result):
        assert iterPower(base,exp) == result

#Test with negative base and even exponential
@pytest.mark.parametrize("neg_base,pos_even_exp,neg_base_result", [
    (-2,2,4),
    (-3,4,81),
    (-9,2,81),
])

class TestIterPowerWithNegativeBaseAndEvenExp:
    def test_iterPower_with_negative_base_and_even_exp(self, neg_base, pos_even_exp,neg_base_result):
        assert iterPower(neg_base,pos_even_exp) == neg_base_result


#Test with negative base and odd exponential
@pytest.mark.parametrize("negative_base,pos_odd_exp,negative_base_result",[
    (-2,3,-8),
    (-3,5,-243),
    (-9,3,-729),
])

class TestIterPowerWithNegativeBaseAndOddExp:
    def test_iterPower_with_negative_base_and_odd_exp(self,negative_base,pos_odd_exp,negative_base_result):
        assert iterPower(negative_base,pos_odd_exp) == negative_base_result



