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
    char* tmp = (char*)malloc(numlen+1);
    tmp[numlen] = '\0';

    if (x == 0) {
        tmp[0] = '0';
        return tmp;
    }

    int insert_idx = 0;
    while (x > 0) {
        char digit = (x % 10) + '0';
        tmp[numlen-insert_idx-1] = digit;
        insert_idx++;
        x /= 10;
    }
    return tmp;
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