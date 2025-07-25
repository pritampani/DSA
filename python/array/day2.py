"""
Modify a given array by replacing each element with the sum or product of their digits based on a given condition
Last Updated : 23 Jul, 2025
Given an array arr[] consisting of N integers, the task is to modify the array elements after performing only one of the following operations on each array elements:

If the count of even digits is greater than the count of odd digits in an array element, then update that element to the sum of all the digits of that element.
Otherwise, update that element to the product of all the digits of that element.
Examples:



Input: arr[] = {113, 141, 214, 3186}
Output: 3 4 7 3186
Explanation:
Following are the operation performed on each array elements:



For element arr[0](= 113): count of even and odd digits are 0 and 3. As count of even < count of odd digit, therefore update arr[0](= 113) to the product of each digit of the number 113 i.e., 1 * 1 * 3 = 3.
For element arr[1](= 141): count of even and odd digits are 1 and 2. As count of even < count of odd digit, therefore update arr[1](= 141) to the product of each digit of the number 141 i.e., 1 * 4 * 1 = 4.
For element arr[2]:(= 214) count of even and odd digits are 2 and 1. As count of even > count of odd digit, therefore update arr[2](= 214) to the sum of each digit of the number 214 i.e., 2 + 1 + 4 = 7.
For element arr[3](= 3186): count of even and odd digits are 2 and 2. As count of even is the same as the count of odd digit, then no operation is performed. Therefore, arr[3](= 3186) remains the same.


After the above operations, the array modifies to {3, 4, 7, 3186}.


Input: arr[] = {2, 7, 12, 22, 110}
Output: 2 7 12 4 0
"""


class Solution:
    def modify_array(self,arr):
        for i in range(len(arr)):
            arr[i]=self.modify_array_util(arr[i])
        return arr

    def modify_array_util(self,n):
        prdct=1
        sm=0
        tempn=n
        even=0
        odd=0
        while n!=0:
            temp=n%10
            if temp%2==0:
                even+=1

            else:
                odd+=1
            sm+=temp
            prdct*=temp
            n//=10
        if even>odd:
            return sm
        elif odd>even:
            return prdct
        else:
            return tempn

a=Solution()

print(a.modify_array([113, 141, 214, 3186]))  # Output: [3, 4, 7, 3186]
print(a.modify_array([2, 7, 12, 22, 110]))    # Output: [2, 7, 12, 4, 2]
print(a.modify_array([100, 101, 111]))        # Output: [1, 0, 1]
print(a.modify_array([2468, 1357, 1234]))     # Output: [20, 105, 1234]