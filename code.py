class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
     

    
'''
I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes, both from right to left:
Odd-index numbers are larger than their neighbors.
Since I put the larger numbers on the odd indexes, clearly I already have:
Odd-index numbers are larger than or equal to their neighbors.
'''
