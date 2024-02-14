#include <stdio.h>
#include <string.h>
#include <stdbool.h> 
#include <stdlib.h>

int lengthOfLongestSubstring(char* s) {
    int len_s = strlen(s);
    int curmax = 0;
    if (len_s < 2) return len_s;

    for (int i = 0; i < len_s; i++) {
        bool exist[128] = {false}; // ASCII 문자의 존재 여부를 추적하는 배열
        int ptr = 0;
        for (int cur = i; cur < len_s; cur++) {
            if (exist[(unsigned char)s[cur]]) {
                break;
            }
            exist[(unsigned char)s[cur]] = true;
            ptr++;
        }
        if (ptr > curmax) {
            curmax = ptr;
        }
    }
    return curmax;
}
