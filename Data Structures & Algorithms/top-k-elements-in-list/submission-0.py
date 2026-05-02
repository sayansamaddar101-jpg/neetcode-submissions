class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        list1=[[]for i in range(len(nums)+1)]

        for i in range(len(nums)):
            dict1[nums[i]]=dict1.get(nums[i] ,0)+1
        
        for i,j in dict1.items():
            list1[j].append(i)
        
        res=[]
        

        for i in range(len(list1)-1, 0 ,-1):
            for j in list1[i]:
                res.append(j)
                if len(res)== k:
                    return res





        
        