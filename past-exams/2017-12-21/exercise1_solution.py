from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
             cache[args] = func(*args)
        return cache[args]
    return wrap



def lopal(S):
    """ Takes a string `S` in input and returns the length of the longest palindrome contained in it.
    """
    @memo
    def dp(i,j):
        if i == j:
            return 1
        elif j == i - 1:
            return 0
        elif S[i] == S[j] and dp(i+1,j-1) == j - i - 1:
            return j - i + 1 
        else:
            return max(dp(i,j-1), dp(i+1,j))
    return dp(0,len(S)-1)

