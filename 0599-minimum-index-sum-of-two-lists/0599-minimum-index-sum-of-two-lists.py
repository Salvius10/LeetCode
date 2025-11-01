class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result=[]
        min1=len(list1)+len(list2)
        for i in range(len(list1)):
            if list1[i] in list2:
                j=list2.index(list1[i])
                if i+j<min1:
                    min1=i+j
                    result=[list1[i]]
                elif i+j==min1:
                    result.append(list1[i])
        return result
