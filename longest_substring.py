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
        
        '''
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
        
        ############
        
            used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
            
        used[c] = i

    
    return max_length
        
        '''
        
        
        maxlength = 0
        
        start = maxlength
        
        ## usedchar stores the location of chars that have been seen already
        usedchar = {}
        
        for i in range(len(s)):
            # print("I")
            # print(i)
            
            # every time we see a new char, check- have we seen it before?
            if s[i] in usedchar and start <= usedchar[s[i]]:
                ## if we've seen it, update the start to the current char + 1 to advance
                start = usedchar[s[i]]+1
                # print("NEW START")
                # print(start)
            else:
                maxlength = max(maxlength, i - start + 1)
                # print("MAXLEN")
                # print(maxlength)
                
            usedchar[s[i]] = i
            
            # print(usedchar)
        return maxlength
    
    
    
    
    
#         ## iterate through a string
#         ## find all possible substrings
        
#         # check if each substring has a same letter
        
#         ## store substring- maybe in a dict?
        
#         # find the longest substring and return the len()
        
#         ## for element in array:
#         # nested for loop
#         # for second element in array:
#         # if the element is the same (or in the substring we're checking)
        
        
        
#         ## ok how do we get all the substrings
        
# #         substring_list = []
# #         for i in range(len(s)):
# #             substring_list.append(s[i])
# #             for j in range(len(s)):
# #                 substring_list.append(s[j])
                           
                
            
# #         print(substring_list)
#         substring_set = set()
#         seen_char_set = set()
#         i = 0
#         j = 1
#         while i <= len(s):
#             while j <= len(s):
#                 # print("Js")
#                 # print(s[i:j])
#                 # for char in s[i:j]:
#                 #     if char not in s[i:j]:
#                 #         # print("NOT IN IT")
#                 #         # seen_char_set.add(s[j-1])
#                 #         print("ADDING TO SUBSTRING SET")
#                 substring_set.add(s[i:j])
#                 j+=1
                
                
            
#             i+=1
#             j = i
#             # print(s[i:j])
#             # for char in s[i:j]:
#             #     if char not in seen_char_set:
#             #         # print("NOT IN IT")
#             #         seen_char_set.add(s[j-1])
#             substring_set.add(s[i:j])
#             # substring_set.add(s[i:j])
        
#         # print(seen_char_set)
#         # print(substring_set)
        
       
            
#         '''
#         0:0
#         0:1
#         0:2
#         0:3
        
#         1:1
#         1:2
#         1:3
        
        
        
#         '''

#         ## This isn't the most efficient or cleanest code, but I'm just going to iterate through the set for code readability

        

#         ## for each substring in the set:

#         ## if there is a duplicate,

#         ## remove that substring

        

#         # I guess I'm going to create a dict to store all the values in each string

        
# # 97
# #         for substring in substring_set:
# # 98
# #             print(substring)
# # 99
        
# # Your previous code was restored from your local storage.       

# ## OK so now I have a set
        
#         ## This isn't the most efficient or cleanest code, but I'm just going to iterate through the set for code readability
        
#         ## for each substring in the set:
#         ## if there is a duplicate,
#         ## remove that substring
        
#         # I guess I'm going to create a dict to store all the values in each string
        
        
#         cleaned_substrings = []
#         for substring in substring_set:
#             cleaned_substrings.append(substring)
#             duplicate_dict = {}
#             # print(substring)
#             for char in substring:     
#                 if char in duplicate_dict:
#                     duplicate_dict[char]+=1
#                 else:
#                     duplicate_dict[char] = 1
#             # print(duplicate_dict)
            
#             for key, value in duplicate_dict.items():
#                 if value > 1:
#                     # print("DUPLICATE!")
#                     # print(f'SUBSTRING {substring}')
#                     # print(substring)
#                     if substring in cleaned_substrings:
#                         cleaned_substrings.remove(substring)
#             # continue

#                 # else:
#                 #     cleaned_substrings.append(substring)
            
#         # print(cleaned_substrings)
        
        
        
        
        
        
#         ## This gets the longest substring and returns the len
#         max_substring_len = 0
#         for item in cleaned_substrings:
#             # print(len(item))
#             if len(item) > max_substring_len:
#                 max_substring_len = len(item)
        
#         # print(max_substring_len)
        
#         return max_substring_len