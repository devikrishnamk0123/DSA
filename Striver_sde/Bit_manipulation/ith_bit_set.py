class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        b = 1 << k
        res = n & b
        if (res == 0):
            return(False)
        else:
            return(True)
        
