class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:      
        
        ana_dict = {}  #creating a hashmap to the store the sorted str and its unsorted str. 
        
        result = []  #resultant array
        
        for word in strs:  # we are iterating through the str
            key = sorted(word)    #sorting the str and storing it in the key variable 
            key = tuple(key)      # key will be stored as unhashable type so to avoid that we are using tuple.
            if key not in ana_dict:   # if the sorted keu is not in the hashmap we are adding it in the hashmap
                ana_dict[key] = [word]  
                
            else:   #if the sorted word is in hashmap the if condition will fail and in else condition we are adding the string to the sorted key
                ana_dict[key].append(word)  #
                
                
        for k,v in ana_dict.items():  #we are appending the values to the resultant array
            result.append(v)
            
        return result  #returning the result