'''q3 Maximum height of the staircase Given an integer A representing the square blocks.
 The height of each square block is 1.
  The task is to create a staircase of max height using these blocks.
   The first stair would require only one block, the second stair would require
   two blocks and so on.
   Find and return the maximum height of the staircase'''
staircase=int(input("enter the no of blocks"))
steps=2
steps1=0
sum=0
sum1=0
while(sum<staircase):
    sum1=sum1+steps
    if sum1<staircase:
        sum=sum+steps
        steps=steps+1
        steps1+=1

    else:
        break
print(" the no of blocks is used  to make staircase is {} and the maximum height is possible by making arrangement of {} blocks  is {}".format(sum,staircase,steps1))




