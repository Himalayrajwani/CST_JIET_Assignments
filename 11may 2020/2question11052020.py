'''Given an integer array A of N integers, find the pair of integers in the array which have
minimum XOR value. Report the minimum XOR value. You have an array A[] with N elements.
 We have 2 types of operation available on this
array :
. We can split a element B into 2 elements C and D such that B = C + D.
. We can merge 2 elements P and Q as one element R such that R = P^Q i.e XOR of P
and Q. You have to determine whether it is possible to make array A[] containing only 1
element 0 after several splits and/or merge?'''




'sourcecode'


def mxor(a1, n):


    a1.sort();

    mxor = 999999
    xorop = 0


    for i in range (0, n-1):
        for j in range (i+1, n-1):


            xorop = a1[i] ^ a1[j]
            mxor = min(mxor, xorop)
    return mxor

a1 = [ int(i) for i in input().split()]

obj = len(a1)

print(mxor(a1, obj))
