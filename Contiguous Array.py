# TC: O(n) where n is the length of the array
# SC: O(n) because, we can have a hashmap of size n in the worst case

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hashmap = {0:-1}
        rsum = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                rsum -= 1
            else:
                rsum += 1
            
            if rsum not in hashmap:
                hashmap[rsum] = i
            
            else:
                length = max(length, i - hashmap[rsum])
                
        return length
                
        
        
        