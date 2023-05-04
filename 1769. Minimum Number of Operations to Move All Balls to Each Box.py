class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lis=[0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    lis[i]+=abs(i-j)
        return lis
