class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # MAP={}
        # for i in nums:
        #     MAP[i]=MAP.get(i,0)+1
        # for i in MAP.values():
        #     if i>1:
        #         return True
        # return False

        num1=set(nums)
        if len(nums)==len(num1):
            return False
        
        return True