class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B:
            return len(set(A)) < len(A)
        pairs = [(a, b) for a, b in zip(A, B) if a != b]
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


""" 처음에 구구절절 짜서 한시간 날려먹은 코드
테스트 케이스 24번째에서 막힘

class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        st = ['0' for _ in range(len(s))]
        goal = list(goal)
        for i in range(len(s)):
            for j in range(i+1, len(goal)):
                if s[i] == goal[i]:
                    st[i] = s[i]
                    continue
                elif s[i] == goal[j] and s[j] == goal[i]:
                    st[i] = s[j]
                    st[j] = s[i]
                    if st == goal: 
                        return True
                    else: 
                        return False
        
        return False
"""
