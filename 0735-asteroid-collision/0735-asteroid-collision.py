class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result=[]
        for i in asteroids:
            alive=True
            while result and result[-1]>0 and i<0:
                if abs(result[-1])<abs(i):
                    result.pop()
                    continue
                elif abs(result[-1])==abs(i):
                    result.pop()
                    alive=False
                    break
                else:
                    alive=False
                    break
            if alive:
                result.append(i)
        return result