#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* reverse(const char *s) {
    int len = strlen(s);
    char* reversed = malloc(len + 1);
    if (reversed == NULL) {
        return NULL; // Memory allocation failed
    }
    for (int i = 0; i < len; i++) {
        reversed[i] = s[len - i - 1];
    }
    reversed[len] = '\0';
    return reversed;
}


int countDigits(int x) {
    if (x == 0) return 1; 
    int count = 0;
    while (x != 0) {
        x /= 10; 
        count++; 
    }
    return count;
}

char* intToString(int x) {
    int numlen = countDigits(x);
    bool isNegative = x < 0;
    if (isNegative) {
        x = -x; 
        numlen++; 
    }
    
    char* str = (char*)malloc(numlen + 1); 
    if (!str) return NULL; 
    str[numlen] = '\0'; 

    if (x == 0) {
        str[0] = '0';
        return str;
    }

    int i = numlen - 1;
    while (x > 0) {
        str[i--] = (x % 10) + '0';
        x /= 10;
    }

    if (isNegative) {
        str[i] = '-';
    }

    return str;
}
bool isPalindrome(int x) {
    if (x < 0) return false;
    char* cur = intToString(x);
    char* currev = reverse(cur);    
    bool result = strcmp(cur, currev) == 0;
    free(cur); 
    free(currev); 
    return result;    
}




