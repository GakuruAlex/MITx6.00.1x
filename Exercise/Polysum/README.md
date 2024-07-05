# function  polysum that takes 2 arguments, n and s #

This function should sum the area and square of the perimeter of the regular polygon

## Area of regular Polygon ##

Area = (0.25*n*s²) / (tan(π/n))

## Perimeter of regular Polygon ##

Perimeter = s * n

## Return ##

the sum, rounded to 4 decimal places

### Tests ##

Using pytest

polysum(51, 47) = 6202251.5755
polysum(11, 50) = 325914.0998
polysum(87, 40) = 13073696.096
polysum(83, 60) = 26773010.5575
polysum(44, 54) = 6093857.0814
polysum(79, 73) = 35903504.2705
polysum(1, 96) = -1.881358773488106e+19
polysum(41, 50) = 4536269.5694
