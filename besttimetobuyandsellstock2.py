class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print(prices)
        
        
        ## take the first element in list
        ## find the diff with the next element
        ## if the diff is positive, save the diff
        ## if it's negative, do nothing
        ## move on to next element until end of array
        
        i=0
        max_profit = 0

        while i < len(prices)-1:
            print(i)
            if prices[i] < prices[i+1]:
                max_profit+=prices[i+1]-prices[i]
            i+=1
        
        
        
        return max_profit
