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

void del_space_and_lowercase(char s[]){
    int length = strlen(s);
    char* tmp = (char*)malloc(length + 1); 
    int k = 0;
    for (int i = 0; i < length; i++) {
        if (isAlnum(s[i])) {
            tmp[k++] = (s[i] >= 'A' && s[i] <= 'Z') ? s[i] + 32 : s[i];
        }
    }
    tmp[k] = '\0';
    strcpy(s, tmp);
    free(tmp); 
}

bool isPalindrome(char* s) {
    del_space_and_lowercase(s); 

    int start = 0;
    int end = strlen(s) - 1;
    while (start < end){
        if (s[start] != s[end]) {
            return false;
        }
        start += 1;
        end -= 1;
    }
    return true;
}