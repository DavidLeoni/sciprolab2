
def stairs(n):
    """ Takes an integer n >= 0 in input and returns the number of ways
        a child can go down a staircase of n steps. Each jump can be at most 4 steps long.

        If n = 0, there is exactly 1 way to descend the stair 
        if n < 0, return 0
    """
    if n < 0:
        return 0

    L = [1, 1]
    for i in range(2, n+1):
        total = 0
        for k in range(max(0, i-4),i):
            total = total + L[k]
        L.append(total)
    return L[n]


