class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        input: array that contains n+1 ints
        each int is between 1:n
        prove that one duplicate number must exist
        assume only one duplicate number
        find the duplicate
        
        can't modify the array (read only)
        o(1) space
        0(n^2) runtime
        
        there is only one duplicate, but it could be in there many times
        '''
        
        # I'd like to create a set, but this would be more space
        
        # nested for loops are out because it needs to be less than n^2 runtime
        
        # Dicts might be out too (more space)
        
        # basically I need to return one value, and keep a tally somewhere that doesn't take up much space. What about a dict that has number of occurences instead of the int as the key? mmm that woudl prob take up the same amount of space
        
        # print(nums)
        
       ## if there's only 
    
        tally_dict = {}
        for item in nums:
            if item in tally_dict:
                tally_dict[item] += 1
            else:
                tally_dict[item] = 1
        
        print(tally_dict)
        
        for key, value in tally_dict.items():
            print(value)
            if value >= 2:
                return key