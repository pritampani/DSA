def firsercf(arr,key):
    l=0
    r=len(arr)-1
    ans=-1
    while r>l:
        mid=(l+r)//2
        if arr[mid]==key:
            ans=mid
            r=mid-1

        elif arr[mid]>key:
            r=mid-1
        else:
            l=mid+1
    return ans


arr=[1,2,3,3,3,4,5,6,6,6,6,7,8]
print(firsercf(arr,6))
