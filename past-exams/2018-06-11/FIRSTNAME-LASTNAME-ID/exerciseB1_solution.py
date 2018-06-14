import math

def  maxRestRic(L, i, r, DP):
	if i==0 and r>0:
		return -math.inf
	if r < 0:
		return -math.inf
	if r == 0:
		return 0
	if DP[i][r]<0:
		DP[i][r] = max(maxRestRic(L, i-1, r, DP), maxRestRic(L, i-1, r-L[i-1], DP) + 1)
	return DP[i][r]

def maxRest(L,R):
    """ Takes 

            L: a list of coins where each element represents the value of the coin
               -  elements are integer > 0 
               - list can be empty
            R: an integer rest R
               - may be negative, zero, or positive.

        Return the maximum number of coins to add so the sum is R
            - if it is impossible to find coins such that sum is equal R, return minus infinity
    """
    DP = [[-1]*(R+1) for i in range(len(L)+1)]
    return maxRestRic(L,len(L),R, DP)


