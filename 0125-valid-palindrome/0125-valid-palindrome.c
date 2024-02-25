#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

bool isAlnum(char c) {
    if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
        return true;
    }
    return false;
}

// given s is array of chars
bool isPalindrome(char* s) {
    int memlen = strlen(s);
    char* tmp = (char*)malloc(memlen+1);
    int insert_idx=0;
    for (int i=0; i < memlen; i++){
        if (!isAlnum(s[i])) continue;
        if (s[i] >= 'A' && s[i] <= 'Z') {
            tmp[insert_idx++] = s[i] +32;
        }
        else {
            tmp[insert_idx++] = s[i];
        }
    }
    tmp[insert_idx] = '\0';
    strcpy(s, tmp);
    free(tmp);
    
    
    int start=0;
    int end = strlen(s)-1;
    while (start < end) {
        if (s[start] != s[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}
