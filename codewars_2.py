n = 37
def show_sequence(n):
    """
    Sum function, creates raw of 0+1+2+3+..+n
    :param n:
    :return result of string:
    """
    if n < 0:
        return("%d<0" % n)
    elif n == 0:
        return("0=0")
    elif n > 0:
        result = "0"
        x = 1
        sum = 0
        while x <= n:
            result += "+%d" % x
            sum += x
            x += 1
        result += " = %d" % sum
    return result
print(show_sequence(n))