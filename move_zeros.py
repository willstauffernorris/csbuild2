class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        input: array nums
        
        move all the 0's to the end while maintaining order of the rest of it
        
        do this in-place
        '''
        
        ## ok so this seems like I just iterate through nums
        ## if an item is 0, just move it to the end of the list
        
        
        for item in nums:
            if item == 0:
                nums.remove(item)
                nums.append(item)
                
        # print(nums)
        return nums
    