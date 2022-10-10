class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        rsumhashmap = {0:1}  # we are creating a hashmap to store the running sum and its occurences. to handle the first element we are appending the key 0 and value 1
        
        count = 0 #to calculate the occurence's count
        rsum = 0
        
        
        for i in range(len(nums)):  #we are iterating through the nums list
            rsum+=nums[i]           #we are calculating the rsum
            compliment = rsum-k     # and we are subtracting the rsum with the target and storing it in the compliment
            
            if compliment in rsumhashmap:   #if the complimnet is in the hashmap we are increasing the count
                count+=rsumhashmap[compliment]
                
            if rsum in rsumhashmap:   #if the rsum  is present in the hashmap we are increasing the counter 
                rsumhashmap[rsum]+=1
            else:
                rsumhashmap[rsum] =1  #if the rsum is not present in the hashmap we are keeping the value as 1
                
        return count  #returning the count
                    
                
                
            
        