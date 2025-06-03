class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_lst="".join([str(n) for n in digits])
        result=int(str_lst)+1
        return list([int(n) for n in str(result)])

        