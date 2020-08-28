class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        input: array of integers 'nums', sorted in ascending order AND integer 'target'
        
        nums is rotated around a pivot point
        
        search for a target in nums
        return the target's index
        
        else return -1
        
        
        ints can be negative
        all values in nums are unique
        
        '''
        
        print(nums)
        print(target)
        
        ## The easiest solution will just be to iterate through the list, starting at the beginning. When I find the target, return its index
        
        ## This also is a good candidate for a binary search tree, but with the twist that it's pivoted.
        
        # I'll try the easy solution first and then try for the binary search tree
        
        for item in nums:
            if item == target:
                return nums.index(item)
        return -1
    
        # worked, no prob
        
        
        ## binary search
        
        # My first thought is to un-pivot the array
        
        # this might be another binary search: try and find the pivot point
        # if there's a place where the next item is not in the sequence, that's the pivot
        
        # then perform a binary search on it
        
        '''
        class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
        '''
        
        if not nums:
            return -1
        low, high = 0, len(nums)-1
        
        
        # binary search
        while low <=high:
            mid = (low + high) /2
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                ## this is the logic to do the twist
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid +1
                else:
                    high = mid -1
        return -1
                
        
        
        
        
        