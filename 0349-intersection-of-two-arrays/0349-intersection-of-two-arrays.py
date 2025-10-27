class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        count={}
        arr=[]
        for i in nums1:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for j in nums2:
            if j in count:
                count[j]+=1
            else:
                count[j]=1
        for key,val in count.items():
            if val==2:
                arr.append(key)
        return arr