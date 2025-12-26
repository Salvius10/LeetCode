class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        dic1={}
        dic2={}
        result=[]
        res1=[]
        res2=[]
        for i in range(len(nums1)):
            if nums1[i] not in dic1:
                dic1[nums1[i]]=1
            else:
                dic1[nums1[i]]+=1
        
        for i in range(len(nums2)):
            if nums2[i] not in dic2:
                dic2[nums2[i]]=1
            else:
                dic2[nums2[i]]+=1
        for i in range(len(nums1)):
            if nums1[i] not in dic2:
                res1.append(nums1[i])
            else:
                continue
        for i in range(len(nums2)):
            if nums2[i] not in dic1:
                res2.append(nums2[i])
            else:
                continue
        result.append(res1)
        result.append(res2)
        return result
        
        