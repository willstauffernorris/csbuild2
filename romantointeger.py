class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        
        ## make a dict of what letter == what value
        
        
        roman_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
             }
        
        ## write an elif chain to handle the special cases
        numeric = 0
        i=0
        while i < len(s):
            print(i)
            if i<(len(s)-1):
                print("EXISTS")
                if s[i] == 'I' and s[i+1] == 'V':
                    numeric += 4
                    i+=1
                elif s[i] == 'I' and s[i+1] == 'X':
                    numeric += 9
                    i+=1
                elif s[i] == 'X' and s[i+1] == 'L':
                    numeric += 40
                    i+=1
                elif s[i] == 'X' and s[i+1] == 'C':
                    numeric += 90
                    i+=1
                elif s[i] == 'C' and s[i+1] == 'D':
                    numeric += 400
                    i+=1
                elif s[i] == 'C' and s[i+1] == 'M':
                    numeric += 900
                    i+=1
                else:
                    numeric += roman_dict[s[i]]
            else:
                numeric += roman_dict[s[i]]
            
            i+=1
            print(numeric)
            
            
#         for letter in s:
#             # print(letter)
            
            
#             # if letter == 'I':
#             #     if 
                
#             numeric += roman_dict[letter]
                
                
                
        '''
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        '''
        # print(numeric)
        return numeric
                
