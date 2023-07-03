class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B:
            return len(set(A)) < len(A)
        pairs = [(a, b) for a, b in zip(A, B) if a != b]
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
