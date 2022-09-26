from os import *
from sys import *
from collections import *
from math import *

def houseRobber(valueInHouse):
    # Write your function here.
    dp = [-1] * len(valueInHouse)
    def helper(valueInHouse,dp,index):
        if (index == 0):
            dp[index] = valueInHouse[0]
            return(dp[index])
        if (dp[index] != -1):
            return(dp[index])
        if ((index-2) >= 0):
            second = helper(valueInHouse,dp,index-2)
            if (index != 2 and index != len(valueInHouse)-1):
                second += valueInHouse[index]
            first = helper(valueInHouse,dp,index-1)
            if (index == len(valueInHouse)-1 and index != 2):
                first = first+valueInHouse[0]
            dp[index] = max(first,second)     
            return(dp[index])
        else:
            first = helper(valueInHouse,dp,index-1)
            dp[index] = max(first,valueInHouse[index])
            return(dp[index])
    result = helper(valueInHouse,dp,len(valueInHouse)-1)
    return(result)
       
