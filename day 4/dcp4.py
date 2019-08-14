"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""


def za(arr,i=0):
    if arr[i]>0 :
        return i
    else :
       return za(arr,i+1)
def alpha(arr):
    arr.sort()
    p=za(arr)
    j=1
    for k in range(p,len(arr)):
        if arr[k]!=j:
            return j
        if k==len(arr)-1:
            return j+1
        if arr[k]!=arr[k+1]:
                j+=1
    return j
a=[-1,2,1,0]
print alpha(a)
