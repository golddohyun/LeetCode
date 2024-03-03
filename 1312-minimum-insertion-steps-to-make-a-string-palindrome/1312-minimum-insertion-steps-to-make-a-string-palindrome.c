#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// int strLength(char* s) {
//     int length = 0;
//     while (s[length] != '\0') length++;
//     return length;
// }

int minInsertions(char* s) {
    int n = strlen(s);
    int **dp = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dp[i] = (int*)malloc(n * sizeof(int));
        memset(dp[i], 0, n * sizeof(int)); 
    }

    for (int left = n - 1; left >= 0; left--) {
        dp[left][left] = 1;
        for (int right = left + 1; right < n; right++) {
            if (s[left] == s[right]) {
                dp[left][right] = 2 + dp[left + 1][right - 1];
            } else {
                dp[left][right] = (dp[left][right - 1] > dp[left + 1][right]) ? dp[left][right - 1] : dp[left + 1][right];
            }
        }
    }

    int result = n - dp[0][n - 1];

    for (int i = 0; i < n; i++) {
        free(dp[i]);
    }
    free(dp);

    return result;
}