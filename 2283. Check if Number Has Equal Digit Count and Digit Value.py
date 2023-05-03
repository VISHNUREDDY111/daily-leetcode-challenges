from collections import Counter 
from collections import OrderedDict
class Solution:
    def digitCount(self, num: str) -> bool:
        count=Counter(num)
        for i in range(len(num)):
            if str(i) not in count.keys():
                count[str(i)]='0'
        dict1 = OrderedDict(sorted(count.items()))
        l1=list(num)
        l2=list(map(str,dict1.values()))
        print(l1,l2)
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False
        return True
        return l1==dict1.values()
        
