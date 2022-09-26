from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp = [-1] * len(nums)
    
    def helper(nums,dp,index):
        if (dp[index] != -1):
            return(dp[index])
        if (index == 0):
            dp[index] = nums[index]
            return(dp[index])
        if (index == 1):
            dp[index] = max(nums[0],nums[1])
            return(dp[index])
        if (index >= 2):
            two = helper(nums,dp,(index-2))
            two += nums[index]
            one = helper(nums,dp,(index-1))
            dp[index] = max(one,two)
            return(dp[index])
    
    max_sum = helper(nums,dp,len(nums)-1)
    return(max_sum)

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
