"""
Count greater elements on the left side of every array element

Given an array arr[] of distinct integers of size N, the task is to print the count of greater elements on the left side of each array element.

Examples :

Input: arr[] = {12, 1, 2, 3, 0, }
Output: 0 1 1 1 4
Explanation:
For index 0, no greater element exists on the left side.
For index 1, {12} is greater element on the left side.
For index 2, {12} is greater element on the left side.
For index 3, {12} is greater element on the left side.
For index 4, {12, 1, 2, 3} are greater elements on the left side.
Therefore, the output is 0 1 1 1 4.



Input: arr[] = {5, 4, 3, 2, 1}
Output: 0 1 2 3 4
"""


class Soluton:
    def count_greater_elements_left(self,arr):
    

        St = set()
        countLeftGreater = [0] * (N)
        for i in range(N):
            St.add(arr[i])
            it = 0
            for st in St:
                if (arr[i] < st):
                    break

                it += 1

            countLeftGreater[i] = abs(it - len(St))
        return countLeftGreater
