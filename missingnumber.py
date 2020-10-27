class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # print(nums)
        
        ## find the int that is missing
        
        ## find the length of the array
        
        # print(len(nums))
        
        ## so there should be every number from 0 to len(nums)
        
        ## sort the list of nums. iterate through the list. if each number is not exactly one greater than the last number, stop and return that number. end at the last number as determined by len(nums). 
        
        #If no missing num found(only 0 in array, return 1)
        
        nums = sorted(nums)
        
        print(len(nums))
        # print(nums[255:])
        
        i = 0
        if nums[i] != 0:
            return 0
        while i < len(nums)-1:
            # print(nums[i])
           
            if nums[i]+1 != nums[i+1]:
                print(nums[i])
                return nums[i]+1
            i+=1
        return len(nums)
        
