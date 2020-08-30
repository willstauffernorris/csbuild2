class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        input: non empty array of ints
        every element appears twice except one
        return the one that only appears once
        
        linear runtime
        '''
        
        print(nums)
        
        ## sounds like I could use a dictionary to keep track of how many times I've seen a number
        
        seen_dict = {}
        
        for item in nums:
            if item in seen_dict:
                seen_dict[item] += 1
            else:
                seen_dict[item] = 1
        print(seen_dict)
        
        for key, value in seen_dict.items():
            if value == 1:
                return key