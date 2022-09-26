def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    # levels is an array that stores the no of ways to reach each index level.
    # for each level the no of ways to reach that level is either by taking 1 jump from previous level or by taking 2 jumps from the 2previous level. The total will be the sum of the 2 ways.
    #time complexity : O(N) Space complexity is: O(N)
    #space complexity can be made constant by removing the array levels and storing the current ways in a variable
    levels = [0] * (nStairs+1)
    if (nStairs == 0):
        #levels[0] = 1 #no of ways to reach level 0 is 1
        return(1)
    if(nStairs == 1):
        return(1)
        #levels[1] = 1 #no of ways to reach level1 is 1
    first_previous = 1
    second_previous = 1
    
    
    for i in range(2,len(levels)):
        current = first_previous + second_previous
        current = current % ((10**9)+7)
        second_previous = first_previous
        first_previous = current
        #levels[i] = levels[i-1] + levels[i-2]
        #levels[i] = levels[i] % ((10**9)+7)
    #return(levels[nStairs])
    return(current)
    
    
