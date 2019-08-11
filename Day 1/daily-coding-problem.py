
"""This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""



def func(mylist,K):
    for i in range(0,len(mylist)-1):
        for j in range(i+1,len(mylist)):
            if mylist[i]+mylist[j]==K:
                print mylist[i] ,"and" , mylist[j]

A=[10,15,3,7]
b=17

func(A,b)
