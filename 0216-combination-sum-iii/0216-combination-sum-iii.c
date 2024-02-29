#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define RANGE 10

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void backtrack(int **res, int *tmp, int k, int n, int *row, int i, int sum, int j) {
    if (sum == n && j == k) {
        for (int i = 0; i < k; i++)
            res[*row][i] = tmp[i];
        (*row)++;
        return;
    } else if (j >= k || sum > n)
        return;
    while (sum + i <= n && i <= 9) {
        tmp[j] = i;
        backtrack(res, tmp, k, n, row, i+1, sum + i, j + 1);
        i++;
    }
}

int** combinationSum3(int k, int n, int* returnSize, int** returnColumnSizes)
{
    int **res = malloc(sizeof(int*) * 1000);    
    for (int i = 0; i < 1000; i++)
        res[i] = malloc(sizeof(int) * k);
		
    int tmp[1000];
    *returnSize = 0;
    backtrack(res, tmp, k, n, returnSize, 1, 0, 0);
    
    if (*returnSize > 0)
        *returnColumnSizes = malloc(sizeof(int) * *returnSize);
    for (int i = 0; i < *returnSize; i++)
        (*returnColumnSizes)[i] = k;
        
    return res;
}