
#include <stdlib.h>
#include <string.h>

void swap(int* a, int* b) {
    const int temp = *a;
    *a = *b;
    *b = temp;
}

void copy_array(int* dst, const int* src, int size) {
    for (int i = 0; i < size; i++) {
        dst[i] = src[i];
    }
}

int factorial(int n) {
    int answer = 1;
    for (int i = 2; i <= n; i++) {
        answer *= i;
    }
    return answer;
}

void backtrack(int* nums, int numsSize, int* tempArr, int tempArrSize, int** result, int* used, int* resultSize, int** returnColumnSizes){
    if (tempArrSize == numsSize) {
        result[*resultSize] = (int*)malloc(numsSize * sizeof(int));
        copy_array(result[*resultSize], tempArr, numsSize);
        (*resultSize)++;
        return;
    }
    for (int i = 0; i < numsSize; i++) {
        if (used[i]) continue;
        used[i] = 1;
        tempArr[tempArrSize] = nums[i];
        backtrack(nums, numsSize, tempArr, tempArrSize + 1, result, used, resultSize, returnColumnSizes);
        used[i] = 0;
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = factorial(numsSize);
    int* used = (int*)calloc(numsSize, sizeof(int));
    int* tempArr = (int*)malloc(numsSize * sizeof(int));
    int** result = (int**)malloc(*returnSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc(*returnSize * sizeof(int));

    if (*returnColumnSizes == NULL) {
        *returnSize = 0;
        return NULL;
    }

    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = numsSize; 
        result[i] = (int*)malloc(numsSize * sizeof(int));
    }

    *returnSize = 0; 
    backtrack(nums, numsSize, tempArr, 0, result, used, returnSize, returnColumnSizes);

    free(used);
    free(tempArr);

    return result;
}