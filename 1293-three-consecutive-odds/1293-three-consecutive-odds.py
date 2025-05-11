class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        j=1
        k=2
        while k<len(arr):
            if arr[i]%2!=0 and arr[j]%2!=0 and arr[k]%2!=0:
                return True 
                break
            i+=1
            j+=1
            k+=1
        return False
            
                

