# Author: Raed K
# Date: 7/17/2024

def helper(DNA1, DNA2, m, n, memo):
    if m < 0 or n < 0:
        return 0

    # return the computation if already in the memo
    if (m, n) in memo:
        return memo[(m, n)]
    
    if DNA1[m] == DNA2[n]:
        # update memo
        memo[(m, n)] = 1 + helper(DNA1, DNA2, m-1, n-1, memo)

    else:
        # update memo with max
        memo[(m, n)] = max(helper(DNA1, DNA2, m-1, n, memo), helper(DNA1, DNA2, m, n-1, memo))

    return memo[(m, n)]

def dna_match_topdown(DNA1, DNA2):
    memo = {}
    return helper(DNA1, DNA2, len(DNA1)-1, len(DNA2)-1, memo)

def dna_match_bottomup(DNA1, DNA2):
    m = len(DNA1)

    n = len(DNA2)

    # init cache
    cache = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                cache[i][j] = 0

            elif DNA1[i-1] == DNA2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1

            else:
                cache[i][j] = max(cache[i-1][j] , cache[i][j-1])
   
    # return bottom right of table
    return cache[m][n]



