class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap = {}  #we are creating hashmap to map the two strings
        
        seen = set()  #we are creating a hashset to store the string if it is not in the hashmap
        
        for i in range(len(s)):   #setting the range for forloop
            if s[i] not in hashmap:  #if the str s is not in hashmap we are adding str s and str t to the hash map
                if t[i] in seen:    #checking the whether the t[i] in set. if it is there in seeen it is not isomorphic so we are returning false
                    return False
                hashmap[s[i]] = t[i]  #we are mapping str s and str t in hashmap
                seen.add(t[i])  # after ading in hashmap we are adding the value of hasmap in set
                
                
                
            else:
                if hashmap[s[i]] != t[i]:  #if the str s is in hashmap the above if condition will fail and comes to the else statement and the hashmap value is not equal to the str t it means the str t is already mapped with some othe str in hashmap so we are returning false
                    return False
                
        return True
        