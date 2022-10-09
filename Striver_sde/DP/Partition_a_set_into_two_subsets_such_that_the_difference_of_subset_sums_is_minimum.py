def minSubsetSumDifference(arr, n):
    # Write your code here.
    # Return the minimum difference in the form of an integer.
    total_sum = 0 
    for num in arr:
        total_sum += num
    min_difference = total_sum
    dp = [[-1 for i in range(total_sum+1)]for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    for s in range(total_sum+1):
        dp[0][s] = False
    if (arr[0] <= total_sum):
        dp[0][arr[0]] = True
    for index in range(1,n):
        for target in range(total_sum+1):
            result_not_including = dp[index-1][target]
            
            if (arr[index] <= target):
                result_including = dp[index-1][target-arr[index]]
            else:
                result_including = False
            dp[index][target] = result_not_including or result_including
    for sums in range(total_sum+1):
        current_sum_possible = dp[n-1][sums]
        if (current_sum_possible == True):
            remaining_sum = total_sum - sums
            difference = abs(sums-remaining_sum)
            min_difference = min(difference,min_difference)
    return(min_difference)
