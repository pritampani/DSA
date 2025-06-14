# def issort(arr, k=0):
#     if k == len(arr) - 1:
#         return True
    
#     if arr[k] > arr[k + 1]:
#         return False
    
#     return issort(arr, k + 1)
# a=[1,2,3,4,5,6,22]
# print(issort(a))





# def arrsum(arr,k=0):
#     c=0
#     if len(arr)==k:
#         return c
#     else:
#         c+=arr[k]
#         k+=1
#     return c + arrsum(arr,k)

# a=[1,2,3,4,5]
# print(arrsum(a))




# def searcharr(arr,key,k=0):
#     if key not in arr:
#         return False

#     if arr[k]==key:
#         return True
#     return searcharr(arr,key,k+1)

# arr=[1,2,3,5,6,0,6,83,3,3,9]
# print(searcharr(arr,9))




# binary search

def search(arr, key):
    arr.sort()
    h = len(arr) - 1
    l = 0
    while l <= h:
        mid = (h + l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            h = mid - 1
        else:
            l = mid + 1
    return -1

arr=[1,5,3,2,8,7,4,8,3,2]
search(arr,7)