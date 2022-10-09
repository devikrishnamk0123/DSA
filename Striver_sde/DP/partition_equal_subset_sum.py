class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        length = 0
        for num in nums:
            total_sum += num
            length += 1
        if (total_sum % 2 == 1):
            return(False)
        
        required_sum = total_sum // 2
        
        dp = [[-1 for i in range(required_sum + 1)]for j in range(len(nums))]
        
        for i in range(length):
            dp[i][0] = True
        for t in range(1,required_sum+1):
            dp[0][t] = False
        if (nums[0] <= required_sum):
            dp[0][nums[0]] = True
        
        for index in range(1,length):
            for target in range(required_sum+1):
                result_not_including = dp[index-1][target]
                if (nums[index] <= target):
                    result_including = dp[index-1][target-nums[index]]
                else:
                    result_including = False
                dp[index][target] = result_not_including or result_including
        return(dp[length-1][required_sum])
        
#         def doesSumexist(index,current_sum,array,dp):
#             if (index == 0):
#                 if (array[index] == current_sum):
#                     dp[index][current_sum] = True
#                     return(True)
#                 else:
#                     dp[index][current_sum] = False
#                     return(False)
#             if (dp[index][current_sum] != -1):
#                 return(dp[index][current_sum])
            
#             if (current_sum == array[index]):
#                 dp[index][current_sum] = True
#                 return(True)
            
#             if (array[index] < current_sum):
#                 result_not_including = doesSumexist(index-1,current_sum,array,dp)
#                 dp[index-1][current_sum] = result_not_including
                
                
#                 current_sum -= array[index]
#                 result_including = doesSumexist(index-1,current_sum,array,dp)
#                 dp[index-1][current_sum] = result_including
#                 return(result_not_including or result_including)
#             if (array[index] > current_sum):
#                 result = doesSumexist(index-1,current_sum,array,dp)
#                 dp[index-1][current_sum] = result
#                 return(result)
#         res = doesSumexist(length-1,required_sum,nums,dp)
#         return(res)
