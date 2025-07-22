class Solution:
    def fractionalknapsack(self, val, wt, cap):
        # Pair value, weight and ratio together
        items = []
        for i in range(len(val)):
            items.append((val[i]/wt[i], val[i], wt[i]))  # (ratio, value, weight)
        print(items)
        
        # Sort by ratio in descending order
        items.sort(reverse=True)
        print(items)

        total_value = 0
        for ratio, value, weight in items:
            if cap >= weight:
                total_value += value
                cap -= weight
            else:
                total_value += ratio * cap
                break
        
        return total_value
    

a=Solution()
print(a.fractionalknapsack([60, 100, 120],[10, 20, 30],50))