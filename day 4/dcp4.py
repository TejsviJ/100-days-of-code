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
