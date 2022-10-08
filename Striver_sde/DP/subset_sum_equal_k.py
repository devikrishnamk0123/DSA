from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[-1 for i in range(k+1)]for j in range(n)]
    
#     def doesSumexist(index,current_sum,array,dp):
#         if (index == 0):
#             if (array[index] == current_sum):
#                 dp[index][current_sum] = True
#                 return(True)
#             else:
#                 dp[index][current_sum] = False
#                 return(False)
#         if (array[index] == current_sum):
#             current_sum = 0
#             dp[index][current_sum] = True
#             return(True)
#         if (dp[index][current_sum] != -1):
#             return(dp[index][current_sum])
#         if (array[index] < current_sum):
#             current_sum_after_including = current_sum - array[index]
#             result_including = doesSumexist(index-1,current_sum_after_including,array,dp)
#             dp[index-1][current_sum_after_including] = result_including
#             result_excluding = doesSumexist(index-1,current_sum,array,dp)
#             dp[index-1][current_sum] = result_excluding
#             return(result_including or result_excluding)
#         else:
#             result = doesSumexist(index-1,current_sum,array,dp)
#             dp[index-1][current_sum] = result
#             return(result)
        
    
#    res = doesSumexist(n-1,k,arr,dp)
#    return(res)
#Iterative solution
    for i in range(n):
        dp[i][0] = True
    for t in range(1,k+1):
        dp[0][t] = False
    if (arr[0] <= k):
        dp[0][arr[0]] = True
    for index in range(1,n):
        for target in range(k+1):
            res_not_included = dp[index-1][target]
            
            if (arr[index] <= target):
                res_included = dp[index-1][target-arr[index]]
            else:
                res_included = False
            result = res_not_included or res_included
            dp[index][target] = result
    return(dp[n-1][k])
    


    

