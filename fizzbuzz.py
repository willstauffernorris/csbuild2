class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        return the string representaion of numbers
        for multiples of 3, output 'fizz' instead of number
        multiples of 5, output "buzz"
        numbers that are multiples of 3 and 5, output "FizzBuzz"
    
        '''
        
        # print(n)
        
        ## create an array populated with a number from 1 to n
        # make each of those elements in the array a string
        
        ## do some if/else logic:
        ## if element % 3 == 0: output fizz
        # if 5 output buzz
        # if 3 and 5 output fizzbuzz
        
        fizz_list = [x for x in range(1,n+1)]
        
        for place, element in enumerate(fizz_list):
            if element % 3 == 0 and element % 5 == 0:
                # print("FIZZBUZZ")
                element = "FizzBuzz"
                fizz_list[place] = element
                # print(fizz_list)
            elif element % 3 == 0:
                # print("FIZZ")
                element = "Fizz"
                fizz_list[place] = element
            elif element % 5 == 0:
                element = "Buzz"
                fizz_list[place] = element
            fizz_list[place] = str(element)
        
        # print(fizz_list)
        
        return fizz_list
        