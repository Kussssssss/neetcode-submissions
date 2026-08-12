class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            if i == '+':
                if arr:
                    total = arr[-1] + arr[-2]
                    arr.append(total)
            elif i == 'D':
                if arr:
                    arr.append(arr[-1] * 2)
            elif i == 'C':
                if arr:
                    arr.pop()
            else:
                arr.append(int(i))
        
        return sum(arr)

