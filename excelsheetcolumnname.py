class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(s)
        # print(ord(s))
        # print(ord("B"))
        answer = 0
        
        for letter in s:
            # print(len(s))
            # diff_from_A = ord(letter)-ord("A")
            # answer += diff_from_A
            
            # answer += 26*(answer) + diff_from_A + 1
            
            answer = answer*26 + ord(letter)-ord("A")+1
            # print(diff_from_A + 1)
            print(answer)
        
        return answer

        
