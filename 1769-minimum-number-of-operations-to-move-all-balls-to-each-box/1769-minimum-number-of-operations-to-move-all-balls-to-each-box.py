class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes=list(boxes)
        answers=[0]*len(boxes)
        operation=0
        for i in range(len(answers)):
            operations=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=="1":
                    idx=abs(i-j)
                    operations+=idx
            answers[i]=operations
        return answers
            