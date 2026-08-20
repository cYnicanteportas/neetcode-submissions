class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        valuesDict = dict()

        for num in nums:
            if valuesDict.get(num) is None:
                valuesDict[num] = 1
            else:
                valuesDict[num] = valuesDict[num]+1

    
        for count in valuesDict.values():
            if count > 1:
                return True
 
        return False
        
