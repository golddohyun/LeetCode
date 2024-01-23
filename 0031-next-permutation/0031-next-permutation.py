class Solution(object):
    def reverse_elem(self, nums, left, right) :
        while left<right :
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right-=1
    
    def nextPermutation(self, nums):
        start_idx = -1
        for idx in range(len(nums)-2, -1, -1) :
            if nums[idx] < nums[idx+1] :
                start_idx = idx
                break

        if start_idx < 0 :
            self.reverse_elem(nums, 0, len(nums)-1)
            return nums

        end_idx = 0
        for idx in range(len(nums)-1, -1, -1) :
            if nums[idx] > nums[start_idx] :
                end_idx = idx
                break
        nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
        self.reverse_elem(nums, start_idx+1, len(nums)-1)

        return nums