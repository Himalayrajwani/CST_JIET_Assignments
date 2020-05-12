'''q4)

Count of paths in a grid Given an integer A,
find and return the number of paths in a grid of size (A x A)
that starts from (1, 1) and reaches (A, A) without crossing the major diagonal.'''

'''source code:'''
def numberOfPaths(p, q):
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]

    return dp[q - 1]
print(numberOfPaths(3, 3))
  

