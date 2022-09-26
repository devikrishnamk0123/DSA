from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    def helper(minimum_energy_required,heights,index):
        if (minimum_energy_required[index] != None):
            return(minimum_energy_required[index])
        

        one_step = helper(minimum_energy_required,heights,index-1) + abs(heights[index]-heights[index-1])
        if (index > 1):
            second_step = helper(minimum_energy_required,heights,index-2) + abs(heights[index]-heights[index-2])        
            minimum_energy_required[index] = min(one_step,second_step)
        else:
            minimum_energy_required[index] = one_step
        return (minimum_energy_required[index]) 
    minimum_energy_required = [None] * (n)
    minimum_energy_required[0] = 0
    result = helper(minimum_energy_required,heights,n-1)
    return(result)
        
        
   
