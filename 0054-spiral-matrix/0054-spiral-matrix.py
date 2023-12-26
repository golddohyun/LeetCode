class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                matrix = list(map(list, zip(*matrix)))[::-1]
        return result
