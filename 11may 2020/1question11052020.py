'''Given an array of integers, every element appears twice except for one. Find that single
one. Note: Your algorithm should have a linear runtime complexity. Could you implement it without
using extra memory?'''


arr=[ int(i) for i in input().split()]
l=1
for i in range(len(arr)):
    if arr.count(arr[i])==1 and l==1:
        print(arr[i])
        l=l+1
    else:
        pass
