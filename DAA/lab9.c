#include <stdio.h>
int max(int a, int b)
{
    return (a > b) ? a : b;
}
int main()
{
    int n;
    printf("Enter no. of Items: ");
    scanf("%d", &n);
    int arr[3][n];
    for (int i = 0; i < n; i++)
    {
        arr[0][i] = i;
        printf("Enter Value of %d item: ", i);
        scanf("%d", &arr[1][i]);
        printf("Enter Weight of %d item: ", i);
        scanf("%d", &arr[2][i]);
    }
    int w;
    printf("Enter Knapsack capacity: ");
    scanf("%d", &w);
    int t[n + 1][w + 1];
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= w; j++)
        {
            if (i == 0 || j == 0)
            {
                t[i][j] = 0;
            }
            else if (arr[2][i - 1] <= j)
            {
                t[i][j] = max(arr[1][i - 1] + t[i - 1][j - arr[2][i - 1]], t[i - 1][j]);
            }
            else
            {
                t[i][j] = t[i - 1][j];
            }
        }
    }
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= w; j++)
        {
            printf("%d ", t[i][j]);
        }
        printf("\n");
    }
    printf("Maximum value that can be obtained: %d\n\n", t[n][w]);
    printf("Items selected:\n");
    int i = n, j = w;
    while (i > 0 && j > 0)
    {
        if (t[i][j] != t[i - 1][j])
        {
            printf("Item %d (Value: %d, Weight: %d) is selected.\n", i, arr[1][i - 1], arr[2][i - 1]);
            j -= arr[2][i - 1];
            i--;
        }
        else
        {
            i--;
        }
    }
    return 0;
}
