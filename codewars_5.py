n = 256
def fcn (n):
    """
    Given u0 = 1, u1 = 2 and the relation 6unun+1-5unun+2+un+1un+2 = 0
    calculate un for any integer n >= 0.
    fcn(n) returns un: fcn(17) -> 131072, fcn(21) -> 2097152
    :param n:
    :return: Nvalue of integer
    """
    U = [1, 2]
    U.append(0)
    U[2] = (6*U[0]*U[1])/(5*U[0] - U[1])
    for x in range(2, n+2):
        U.append(0)
        U[x] = (6*U[x-2]*U[x-1])//(5*U[x-2] - U[x-1])
    return U[n]
print(fcn(n))