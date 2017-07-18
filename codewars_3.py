n = 1234
def reverse(n):
    """
    Function for reversing integer without string conversion
    :param n eg 1234:
    :return revVal of integer:
    """
    revVal = ""
    while n > 0:
        revVal += str(n%10)
        n //= 10
    revVal = eval(revVal)
    return int(revVal)
print(reverse(n))