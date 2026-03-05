Class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last= 0, nums[0]
        for i, val in enumerate(nums):
            if val > last[1] and i != 0:
               nums[i] = nums[last[0]+1]
               nums[last[0]+1] = val
               last = last[0]+1, val
        return last[0] + 1
