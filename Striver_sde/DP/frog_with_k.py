number_of_stones, k = map(int, input().split(' '))

heights = list(map(int, input().split(' ')))
minimum_cost = [-1] * (number_of_stones)


def find_minimum_cost(index, heights, dp, k):
    if (index == 0):
        dp[index] = 0
        return(dp[index])
    if(dp[index] != -1):
        return(dp[index])

    min_cost = float('inf')
    i = k
    while(i >= 1):
        if ((index-i) >= 0):
            cost = find_minimum_cost(index-i, heights, dp, k)
            cost += abs(heights[index]-heights[index-i])
            min_cost = min(min_cost, cost)
        i -= 1
    dp[index] = min_cost
    return(dp[index])


min_cost = find_minimum_cost(number_of_stones-1, heights, minimum_cost, k)
print(min_cost)
