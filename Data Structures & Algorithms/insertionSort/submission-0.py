# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        list_pairs = []
        for i in range(len(pairs)):
            
            for j in range(i, 0, -1):
                if pairs[j-1].key > pairs[j].key:
                    pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
                else: break

            list_pairs.append(pairs.copy())
        
        return list_pairs