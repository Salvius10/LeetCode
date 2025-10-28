class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split(" ")
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if (int(a[j+1][-1])<int(a[j][-1])):
                    a[j+1],a[j]=a[j],a[j+1]
        for i in range(len(a)):
            a[i]=a[i].replace(a[i][-1],"")

        a=" ".join(a)
        return a