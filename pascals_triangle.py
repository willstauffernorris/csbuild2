class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ## palindrome patttern
        
        ## each number is the sum of the two numbers directly above it
        
        ## input is the number of rows

        rows = []
        for i in range(numRows):
            if i == 0:
                rows.append([1])
            # don't actually need this base case
            # elif i == 1:
            #     rows.append([1,1])
            else:
                # start with 1
                pascal_list = [1]
                
                # fill in middle bit
                middle_number_count = i-1
                
                for j in range(middle_number_count):
                    row_index = j + 1
                    prev_row = rows[-1]
                    value = prev_row[row_index] + prev_row[row_index-1]
                    pascal_list.append(value)
                        
                # add one on the end
                pascal_list.append(1)
                # pascal_list[i] = rows[i-1]
                rows.append(pascal_list)
        return rows
            