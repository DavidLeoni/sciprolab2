
def stock(V):
    """ Take a list of positive integers as stock quotes, and return an integer. 
        For more info see exam text and tests.
    """

    n = len(V)
    DP = [ [-1]*(i+1) for i in range(n-1)]
    temp = stockRec(V,0,0,DP)
    return temp
	
def stockRec(V,i,k,DP):
    if i==len(V)-1:
        return V[i]*k
    if DP[i][k]<0:
        DP[i][k]=max(
                    stockRec(V, i+1, k, DP),
                    stockRec(V, i+1, k+1, DP) - V[i],
                    stockRec(V, i+1, 0, DP) + k*V[i] )
    return DP[i][k]
		
