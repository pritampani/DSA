#include <stdio.h>
#include <string.h>
int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

void lcs(char a[], char b[])
{
    int i, j, m, n;
    m = strlen(a);
    n = strlen(b);
    int table[m + 1][n + 1];



    for (i = 0; i <= m; i++)
    {
        table[i][0] = 0;
    }



    for (i = 0; i <= n; i++)
    {
        table[0][i] = 0;
    }





    for (i = 1; i <= m; i++)
    {
        for (j = 1; j <= n; j++)
        {
            if (a[i - 1] == b[j - 1])
            {
                table[i][j] = table[i - 1][j - 1] + 1;
            }
            else
            {
                table[i][j] = max(table[i - 1][j], table[i][j - 1]);
            }
        }
    }

    printf("\nLength of Longest Subsequence:%d",table[m][n]);


    // Backtrack to find the LCS and store it in 'lcs' array
    int index = table[m][n];
    char lcs[index +1];
    //to handle the null charater
    lcs[index] = '\0';
    i = m, j = n;
    while (i > 0 && j > 0)
    {
        if (a[i - 1] == b[j - 1])
        {
            // Matched characters, include in LCS
            lcs[index - 1] = a[i - 1];
            i--;
            j--;
            index--;
        }
        else if (table[i - 1][j] > table[i][j - 1])
        {
            // Move to the previous row
            i--;
        }
        else
        {
            // Move to the previous column
            j--;
        }
    }

    
    printf("\nS1 : %s \nS2 : %s \n", a, b);
    printf("LCS: %s\n", lcs);
}
int main()
{
    char S1[20], S2[20];
    printf("Enter String1: ");
    scanf("%s", S1);
    printf("Enter String2: ");
    scanf("%s", S2);
    lcs(S1, S2);
    printf("\n");
    return 0;
}