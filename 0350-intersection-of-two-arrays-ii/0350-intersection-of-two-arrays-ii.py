class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1={}
        count2={}
        a=[]
        for i in nums1:
            if i not in count1:
                count1[i]=1
            else:
                count1[i]+=1
        for j in nums2:
            if j not in count2:
                count2[j]=1
            else:
                count2[j]+=1
        for key in count1:
            if key in count2:
                count=min(count1[key],count2[key])
                a.extend([key]*count)
        return a