"""This problem was asked by Uber.

Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in
the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""

def fun1(index1 , a   , b=[] ):
    p=1

    for i in range(0,len(a)):
        if i!=index1 :
            p*=a[i]
    index1+=1
    b.append(p)
    if index1<len(a):
        fun1(index1,a,b)
    
    return b;

a=[1,2,3,4,5]
z=fun1(0,a)
print z


