from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if n1 > n2:
            return False
        m1:defaultdict[str,int] = defaultdict(int)
        for char in s1:
            m1[char]+=1
        m2: defaultdict[str,int] = defaultdict(int)
        for i in range(n1):
            m2[s2[i]]+=1
        start = 0
        while True:
            if m1 == m2:
                return True
            if start + n1 >= n2:
                break
            
            out_char = s2[start]
            m2[out_char] -= 1
            if m2[out_char] == 0:
                del m2[out_char]
            
            in_char = s2[start+n1]
            m2[in_char] += 1

            start+=1
        return False
        