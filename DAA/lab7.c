#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    char s1[] = "AGGTAB";
    char s2[] = "GXTXAYB";
    int row = strlen(s1)+1;  
    int col = strlen(s2)+1;  
    
    int dmatrix[row][col];

    
    for (int c = 0; c < col; c++) {
        dmatrix[0][c] = 0;
    }
    for (int r = 0; r < row; r++) {
        dmatrix[r][0] = 0;
    }

    
    for (int r = 1; r < row; r++) {
        for (int c = 1; c < col; c++) {
            if (s1[r - 1] == s2[c - 1]) {
                dmatrix[r][c] = dmatrix[r - 1][c - 1] + 1;
            } else {
                dmatrix[r][c] = max(dmatrix[r - 1][c], dmatrix[r][c - 1]);
            }
        }
    }
    printf("lcs will be %d\n", dmatrix[row -1][col-1]);
    return 0;
}
