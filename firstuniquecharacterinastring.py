class Solution:
    def firstUniqChar(self, s: str) -> int:
        print(s)
        
        ### make a hash table to save the counts of each char
        ## go through the string and add letter if you haven't seen it
        ## make its key the index of that letter in the string AND
        ## record the number of times you've seen it
        ## if you've already seen that letter, +=1 the times (ignore index cuz it doesn't matter)
        
        
        ## 
        
        ## 
        
        unique_dict = {}
        
        for letter in s:
            if letter in unique_dict:
                unique_dict[letter]+=1
            else:
                unique_dict[letter]=1
        print(unique_dict)
        
        for item in unique_dict:
            print(item)
            if unique_dict[item] == 1:
                return s.index(item)
        
        return -1
            
        # print(s.index("l"))
