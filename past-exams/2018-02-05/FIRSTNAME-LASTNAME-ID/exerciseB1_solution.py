
def subsetsum(A,S):
    """
    Let A be a list of non-negative integers, and S a target integer value.
    Return True if there exists a subset  of the integers in A whose sum is
    equal to the target value S. Otherwise, return False.

    NOTE:
      - if S = 0, always return True, even with empty array
      - numbers in A may be repeated
    """
    n = len(A)
    DP = [[-1]*(S+1) for k in range(n+1)]
    return sssrec(A,DP,n,S)

def sssrec(A, DP, i, s):
    if s==0:
        return True
    if s<0:
        return False
    if i==0:
        return False
    if DP[i][s] == -1:
        DP[i][s] = sssrec(A,DP,i-1,s-A[i-1]) or sssrec(A,DP,i-1,s)
    return DP[i][s]


