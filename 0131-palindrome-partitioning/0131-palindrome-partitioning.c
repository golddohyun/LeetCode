/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

char* sliceString(const char* str, int start, int end) {
    int len = strlen(str);
    if (start < 0) start = len + start;
    if (end < 0) end = len + end;
    if (start > end || start < 0 || end > len) return NULL;
    int sliceLen = end - start;
    char* result = (char*)malloc(sliceLen + 1); 
    if (!result) return NULL; 
    strncpy(result, str + start, sliceLen); 
    result[sliceLen] = '\0';
    return result;
}


bool isPalindrome_(char* s) {
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


void backtrack(char* s, int start, char** path, int pathLen, char**** result, int* returnSize, int* totCapacity, int** returnColumnSizes) {
    int sLength = strlen(s);
    if (start == sLength) {
        if (*totCapacity <= *returnSize) {
            *totCapacity *= 2;
            *result = (char***)realloc(*result, (*totCapacity) * sizeof(char**));
            *returnColumnSizes = (int*)realloc(*returnColumnSizes, (*totCapacity) * sizeof(int));
        }

        (*result)[*returnSize] = (char**)malloc(pathLen * sizeof(char*));
        for (int i = 0; i < pathLen; i++) {
            (*result)[*returnSize][i] = strdup(path[i]);
        }
        (*returnColumnSizes)[*returnSize] = pathLen;
        (*returnSize)++;
    } else {
        for (int end = start; end < sLength; end++) {
            char* substr = sliceString(s, start, end + 1);
            if (isPalindrome_(substr)) {
                path[pathLen] = substr;
                backtrack(s, end + 1, path, pathLen + 1, result, returnSize, totCapacity, returnColumnSizes);
            } else {
                free(substr);
            }
        }
    }
}

char*** partition(char* s, int* returnSize, int** returnColumnSizes) {
    int totCapacity = 10; 
    char** path = (char**)malloc(strlen(s) * sizeof(char*));
    char*** result = (char***)malloc(totCapacity * sizeof(char**));
    *returnColumnSizes = (int*)malloc(totCapacity * sizeof(int));
    *returnSize = 0;

    backtrack(s, 0, path, 0, &result, returnSize, &totCapacity, returnColumnSizes);

    if (totCapacity > *returnSize) {
        result = (char***)realloc(result, (*returnSize) * sizeof(char**));
        *returnColumnSizes = (int*)realloc(*returnColumnSizes, (*returnSize) * sizeof(int));
    }

    free(path);    
    return result;
}
