class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1={}

        for i in nums:
            dict1[i]=dict1.get(i,0)+1

        for i in dict1.values():
                if i>1:
                    return True
        else:
             return False
        
        