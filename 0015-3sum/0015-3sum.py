class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []

        from collections import Counter
        result = set()
        counter = Counter(nums)
        nums = list(counter.keys())
        pos_item, neg_item = [x for x in nums if x > 0], [x for x in nums if x < 0]

        if counter[0] >= 3:
            result.add((0, 0, 0))

        for n in neg_item:
            for p in pos_item:
                compliment = -(n + p)
                if compliment in counter and ((compliment != n and compliment != p) or counter[compliment] > 1):
                    result.add(tuple(sorted([n, p, compliment]))) 

        return [list(triplet) for triplet in result] 