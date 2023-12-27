class Solution(object):
    def wordcounter(self, nums):
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        return counter

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        wdict = self.wordcounter(nums)
        # Sort the dictionary by value
        sorted_dict = sorted(wdict.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_dict[:k]]