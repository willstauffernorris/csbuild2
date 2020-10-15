class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print(s)
        print(t)
        
        
        ### what defines an anagram?
        
        #it's just the same number of letters, in a diff order
        
        ## go through all of the letters-
        ## maybe make a dictionary of letter counts
        ## if there is any difference between the two dictionaries, it's not an anagram
        first_dict = {}
        for letter in s:
            if letter not in first_dict:
                first_dict[letter] = 1
            else:
                first_dict[letter] += 1
        
        print(first_dict)
        
        second_dict = {}
        for letter in t:
            if letter not in second_dict:
                second_dict[letter] = 1
            else:
                second_dict[letter] += 1
                
        print(second_dict)
        
        if first_dict == second_dict:
            return True
        else:
            return False
        
        
