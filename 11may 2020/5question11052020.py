'''  q5))))
Square Root of Integer
Given an integar A. Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY'''
"source code"
def sqrtSearch(low, high, N) :

    if (low <= high) :

        mid = (low + high) // 2;

        if ((mid * mid <= N) and ((mid + 1) * (mid + 1) > N)) :
            return mid;


        elif (mid * mid < N) :
            return sqrtSearch(mid + 1, high, N);

        else :
            return sqrtSearch(low, mid - 1, N);

    return low;


if __name__ == "__main__" :

    N = 268;
    print(sqrtSearch(0, N, N))



"2 nd method"
def sqrt(A):
    sum=0
    for i in range(1,A):
        if A%i==0:
            sum=sum+i
    if sum!=A:
        A=A**(1/2)
        return int(A)
    else:
        print("press 1 for if you want perfect no square root")
        choice=int(input("enter the choice"))
        if  choice==1:
            A=A**(1/2)
            return int(A)



s=sqrt(int(input()))
print(s)
    

