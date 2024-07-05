from math import tan, pi
def polysum(n, s):
    """_sums the area and perimeter of a polygon_

    Args:
        n (_int_): _Number of sides of the polygon_
        s (_int_): _Length of a side of the polygon_

    Returns:
        sum (_float_): _Sum of the square of perimeter and area of polygon rounded to 4 decimal places_
    """
    def area_of_polygon(n, s):
        """_Find area of polygon_
        """

        return 0.25 * n * pow(s, 2) / tan(pi/n)
    def sum_of_polygon(n, s):
        """_Find square of sum of polygon_
        """

        return pow(n * s, 2)
    return  round(area_of_polygon(n, s) + sum_of_polygon(n, s), 4)

def main() -> None:

    print(polysum(45, 30 ))

if __name__ == "__main__":
    main()