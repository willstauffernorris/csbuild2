class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        input: string
        find length of longest substring w/o repeating characters
        
        return length
        
        '''
        ## iterate through a string
        ## find all possible substrings
        
        # check if each substring has a same letter
        
        ## store substring- maybe in a dict?
        
        # find the longest substring and return the len()
        
        ## for element in array:
        # nested for loop
        # for second element in array:
        # if the element is the same (or in the substring we're checking)
        
        
        
        ## ok how do we get all the substrings
        
#         substring_list = []
#         for i in range(len(s)):
#             substring_list.append(s[i])
#             for j in range(len(s)):
#                 substring_list.append(s[j])
                           
                
            
#         print(substring_list)
        substring_set = set()
        seen_char_set = set()
        i = 0
        j = 1
        while i <= len(s):
            while j <= len(s):
                # print("Js")
                print(s[i:j])
                for char in s[i:j]:
                    if char not in seen_char_set:
                        # print("NOT IN IT")
                        seen_char_set.add(s[j-1])
                        print("ADDING TO SUBSTRING SET")
                        substring_set.add(s[i:j])
                j+=1
                
                
            
            i+=1
            j = i
            print(s[i:j])
            for char in s[i:j]:
                if char not in seen_char_set:
                    # print("NOT IN IT")
                    seen_char_set.add(s[j-1])
                    substring_set.add(s[i:j])
            # substring_set.add(s[i:j])
        
        print(seen_char_set)
        print(substring_set)
        
        max_substring_len = 0
        for item in substring_set:
            # print(len(item))
            if len(item) > max_substring_len:
                max_substring_len = len(item)
        
        print(max_substring_len)
        
        return max_substring_len
            
        '''
        0:0
        0:1
        0:2
        0:3
        
        1:1
        1:2
        1:3
        
        
        
        '''
        ## OK so now I have a set