#include <stdio.h>
#include <stdlib.h>
int main()
{
    int m;
    printf("Enter No Of Activity: ");
    scanf("%d", &m);
    int arr[3][m];
    for (int j = 0; j < m; j++)
    {
        arr[0][j] = j;
        printf("Enter Start Time of %d Activity: ", j);
        scanf("%d", &arr[1][j]);
        printf("Enter End Time of %d Activity: ", j);
        scanf("%d", &arr[2][j]);
    }
    int i, j, temp;
    for (i = 0; i < m - 1; i++)
    {
        for (j = 0; j < m - i - 1; j++)
        {
            if (arr[2][j] > arr[2][j + 1])
            {
                temp = arr[2][j];
                arr[2][j] = arr[2][j + 1];
                arr[2][j + 1] = temp;
                temp = arr[1][j];
                arr[1][j] = arr[1][j + 1];
                arr[1][j + 1] = temp;
                temp = arr[0][j];
                arr[0][j] = arr[0][j + 1];
                arr[0][j + 1] = temp;
            }
        }
    }
    printf("Activity Matrix (Sorted by End Time):\n");
    printf("Index\tStart Time\tEnd Time\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }
    printf("Activity Selection:\n");
    printf("%d ", arr[0][0]);
    int prev = arr[2][0];
    for (int j = 0; j < m; j++)
    {
        if (prev <= arr[1][j + 1])
        {
            printf("%d ", arr[0][j + 1]);
            prev = arr[2][j + 1];
        }
    }
    return 0;
}