class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res=[]
        dic={}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]]=1
            else:
                dic[arr[i]]+=1
        for i in dic.values():
            if i not in res:
                res.append(i)
            else:
                return False
        return True