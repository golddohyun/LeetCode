/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void BackTrack(int** graph, int graphSize, int* graphColSize, int curnode, const int target, int* path, int* used, int pathlength, int*** ans, int* totLen, int* returnSize, int** returnColumnSizes) {
    if (curnode == target) {
        if (*returnSize >= *totLen) {
            *totLen *= 2; 
            *ans = (int**)realloc(*ans, (*totLen) * sizeof(int*)); 
            *returnColumnSizes = (int*)realloc(*returnColumnSizes, (*totLen) * sizeof(int));
        }

        (*ans)[*returnSize] = (int*)malloc(pathlength * sizeof(int));
        memcpy((*ans)[*returnSize], path, pathlength * sizeof(int));
        (*returnColumnSizes)[*returnSize] = pathlength;
        (*returnSize)++;
        return;
    }

    for (int i = 0; i < graphColSize[curnode]; i++) {
        if (!used[graph[curnode][i]]) {
            used[graph[curnode][i]] = 1;
            path[pathlength] = graph[curnode][i];
            BackTrack(graph, graphSize, graphColSize, graph[curnode][i], target, path, used, pathlength + 1, ans, totLen, returnSize, returnColumnSizes);
            used[graph[curnode][i]] = 0;
        }
    }
}



int** allPathsSourceTarget(int** graph, int graphSize, int* graphColSize, int* returnSize, int** returnColumnSizes) {
    (*returnSize) = 0;
    int totLen = 1;
    int** ans = (int**)malloc(totLen * sizeof(int*));
    int* path = (int*)malloc(graphSize * sizeof(int));    
    path[0] = 0;
    int* used = (int*)calloc(graphSize, sizeof(int));
    *returnColumnSizes = (int*)malloc(totLen * sizeof(int));
    
    // int** graph, int graphSize, source, target, path, pathlength, return, returnSize, returnColumnSizes
    BackTrack(graph, graphSize, graphColSize, 0, graphSize-1, path, used, 1, &ans, &totLen, returnSize, returnColumnSizes);

    if (totLen > (*returnSize)) {
        ans = (int**)realloc(ans, (*returnSize) * sizeof(int*));
        *returnColumnSizes = (int*)realloc(*returnColumnSizes, (*returnSize)*sizeof(int));
    }
    free(path);
    free(used);
    return ans;
}
