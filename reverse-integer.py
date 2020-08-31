class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        input: 32 bit int
        reverse digits of int
        
        
        '''
        
        ## couple approaches. I could try some kind of bit shifting, but I'm not sure exactly how to do that.
        
        # or I could split the elements into a list
        
        ## reverse the list
        
        # put the elements back together
        
        # if there was a negative, put the negative back on the front
        
        # if the first char is a 0, ignore it
        if x is 0:
            # print("SDFSDF")
            return 0
        
        ## function must return 0 when reversed int overflows
            
        
        x = str(x)
        # x = x.split()
        
        ## negative number
        if x[0] == "-":
            print("NEG")
            x = x[1:]
            
            x = x[::-1]
            while x[0] is "0":
                x = x[1:]
            x = "-"+x
            print(x)
            
            
        # positive number
        else:
            x = x[::-1]
            
        ## case where new reversed number starts with 0
        
        # print(x[0])
        # print(x[0] is "0")
        # if x[0] is "0":
        #     print("SDGSDF")
            
        while x[0] is "0":
            x = x[1:]
        
        
        print(type(x))
        
        x = int(x)
        
        # if x not in range(-2**31, 2**31-1):
        #     return 0
        
        if x < -2**31:
            return 0
        
        print(-2**31)
        
        if x > (2**31)-1:
            return 0
        
        
        
        return x