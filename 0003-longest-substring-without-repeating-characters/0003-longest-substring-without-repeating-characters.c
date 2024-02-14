#include <stdio.h>
#include <string.h>
#include <stdbool.h> 
#include <stdlib.h>

bool isSubstring(char ch, char* str) {
    for (int i = 0; str[i]; i++) {
        if (str[i] == ch) return true;
    }
    return false;
}

int lengthOfLongestSubstring(char* s) {
    int len_s = strlen(s);
    int curmax = 0;
    if (len_s < 2) {return len_s;}

    for (int i=0; i < len_s; i++) {
        char* tmp = (char*)malloc(len_s + 1); 
        memset(tmp, 0, len_s + 1); // initialize to zero
        int ptr = 0;
        for (int cur=i; cur < len_s; cur++) {
            if (isSubstring(s[cur], tmp)) {
                break;
            }
            tmp[ptr++] = s[cur]; 
        }
        tmp[ptr] = '\0'; 
        if (ptr > curmax) { 
            curmax = ptr; 
        }
        free(tmp); 
    }
    return curmax;
}