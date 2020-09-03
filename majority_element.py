class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        input: array of size n
        find element that appears more than n/2 times
        array is non empty, majority element always exists
        return that element
        
        '''
        
        
        ## sounds like I want to iterate through the array
        ## maybe store the results in a hash table
        # count how many times each elemnt appears
        
        # for each element, if count > n/2, return that element
        
        ## any other ways to do it? probably!
        
        number_counter = {}
        
        for item in nums:
            if item in number_counter:
                number_counter[item] += 1
            else:
                number_counter[item] = 1
                
        print(number_counter)
        
        n = len(nums)
        print(n/2)
        
        for key, value in number_counter.items():
            print(number_counter[key])
            if number_counter[key] > n/2:
                print("FOUND")
                return key
        
        
        
        