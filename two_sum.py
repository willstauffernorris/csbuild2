# import sys
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        input: array of integers
        return indices of (the two numbers that add up to a target)
        '''
        
        ## Each input has only one solution ( that makes it easier!)
        
        ## figure out which two numbers add up to the target
        # print(nums)
        # print(target)
        
        # iterate through the list
        ## can inputs be negative? not sure. Better handle negs just in case.
        
        # probably nested for loops- grab the first element, check it against all other elements.
        # repeat with the second element. Slow, but will work.
        # could cache results for faster runtime.
        result_list = []
        
        # nums_copy = nums.copy()
        # print(nums_copy)
        
#         if len(nums) == 2:
#             if nums[0] + nums[1] == target:
#                 result_list.append(0)
#                 result_list.append(1)
#                 return result_list
#         for item1 in nums:
#             # print("ITEM 1")
#             # print(item1,nums.index(item1))
#             for item2 in nums:
#                 print("ITEM 1")
#                 print(item1,nums.index(item1))
#                 print("ITEM 2")
#                 print(item2,nums.index(item2))
                    
#                 if nums.index(item1) is not nums.index(item2):
#                     if item1+item2 == target:
#                         # print(item1, item2)
#                         # print(nums.index(item1))
#                         result_list.append(nums.index(item1))
#                         result_list.append(nums.index(item2))
#                         return result_list
#fuck that
        # for item1 in range(len(nums)-1):
        #     for item2 in range(item1+1, len(nums)):
        #         if nums[item1] + nums[item2] == target:
        #             print(item1, item2)
        #             result_list.append(item1)
        #             result_list.append(item2)
        # return result_list
        
        # return the indices of those numbers
        
        ## OK try it with a hash table now
        
        
        # for counter, value in enumerate(nums):
        # print(counter, value)
        
        lookup_table = {}
        # for i, n in enumerate(nums):
        #     if n in lookup_table:
        #         return [lookup_table[n], i]
        #     else:
        #         lookup_table[target-n] = i
                
        for index, value in enumerate(nums):
            # print(lookup_table)
            if value in lookup_table:
                return [lookup_table[value], index]
            else:
                lookup_table[target-value] = index
        
       