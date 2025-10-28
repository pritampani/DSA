#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> targetSumComb(vector<int> &arr, int target)
    {
        vector<vector<int>> ans;
        vector<int> curr;
        int i = 0;
        helper(arr, ans, i, target, curr);
        return ans;
    }

    void helper(vector<int> &arr, vector<vector<int>> &ans, int i, int target, vector<int> &curr)
    {
        // base conditions
        if (target == 0)
        {
            ans.push_back(curr);
            return;
        }
        if (i >= arr.size() || target < 0)
            return;

        // include current element
        curr.push_back(arr[i]);
        helper(arr, ans, i, target - arr[i], curr);
        curr.pop_back();

        // exclude current element
        helper(arr, ans, i + 1, target, curr);
    }
};
