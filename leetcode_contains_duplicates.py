class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        This function determines if there are duplicates in an array.
        
        Input is an array of integers. [1,2,3]
        Output is boolean (True=Duplicate/False=No Duplicate)
        '''
        
        
        '''
        Solution #1
        
        ## This sounds like a good place to use a dictionary
        ## to keep track of how many times a value has appeared.
        
        ## Create a dictionary
        self.duplicate_dictionary = {}
        ## Go through each number in the list
        for element in nums:
            ## If it is, go ahead and return True (Duplicate)
            ## This line must be first, otherwise the element will already be in the             dict when this if is checked.
            if element in self.duplicate_dictionary:
                print(self.duplicate_dictionary)
                return True
            ## If it isnt' in the dictionary, put it in
            if element not in self.duplicate_dictionary:
                # print(element)
                self.duplicate_dictionary[element] = 1
           
        return False
    
        '''    
        
        
        ## After doing some reading on this problem, I'm going to try using a set.
        ## A Python set contains only unique values, 
        ## so I can compare it to the original list
        
        ## create a set
        ## for each number in the input, 
             ## add the number to the set
        #if the length of the original input is greater than the lenght of the set:
            ## There are duplicates
            
        unique_set = set()
        for element in nums:
            unique_set.add(element)
        #print(unique_set)
        
        if len(unique_set) < len(nums):
            return True
        return False
       
        
        