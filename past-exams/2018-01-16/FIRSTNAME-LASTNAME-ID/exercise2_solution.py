from math import sqrt


def squares(n):
    """ Given an integer n, return the minimum number of squares that
        need to be summed together to obtain n.
    """
    return squaresDyn(n) 
    # return squaresMemo(n) # we could use this as well


def squaresRec(DP, n):
	if DP[n]<0:
		DP[n] = n
		for k in range(1, int(sqrt(n))+1):
			temp = squaresRec(DP, n-k*k)+1
			DP[n] = min(DP[n], temp)
	return DP[n]
		
def squaresMemo(n):
	DP = [-1]*(n+1)
	DP[0] = 0
	return squaresRec(DP,n)

def squaresDyn(n):
	DP = [-1]*(n+1)
	DP[0] = 0
	for i in range(1,n+1):
		DP[i] = i
		for k in range(1, int(sqrt(i))+1):
			DP[i] = min(DP[i], DP[i-k*k]+1)
	return DP[n]
