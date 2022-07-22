#TC: O(n)
#SC: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashmap = {0:1}
        
        rsum = 0
        counter = 0
        
        for i in range(len(nums)):
            
            rsum += nums[i]
            
            if (rsum - k) in hashmap:
                counter += hashmap[rsum - k]
                
            if rsum not in hashmap:
                hashmap[rsum] = 1
            else:
                hashmap[rsum] += 1
            
            
        return counter
                
        