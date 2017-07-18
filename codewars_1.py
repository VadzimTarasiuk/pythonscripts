pol_str = "2*x**2 + 3*x - 44"
def calc_pol(pol_str, x = None):
    """
    Func for calculating a Polynomes e.g.:
    calc_pol("2*x**2 + 3*x", 4) == "Result = 44"
    calc_pol("2*x**2 + 3*x - 44", 4) == "Result = 0, so 4 is a root of 2*x**2 + 3*x - 44"
    calc_pol(pol_str) == "There is no value for x"
    :param pol_str:
    :param x:
    :return result of string:
    """
    if x is None:
        return "There is no value for x"
    solveto = pol_str.replace("x", str("(%d)" % x), 2)
    solved = eval(solveto)
    if solved == 0:
        return "Result = %d, so %d is a root of %s" %(solved, x, pol_str)
    else:
        return "Result = %d" % solved
print(calc_pol(pol_str, -1))