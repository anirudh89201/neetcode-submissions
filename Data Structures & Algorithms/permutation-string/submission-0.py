from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        start = 0
        m1:defaultdict[str,int] = defaultdict(int)
        for char in s1:
            if char not in m1:
                m1[char] = 1
            else:
                m1[char]+=1
        m2:defaultdict[str,int] = defaultdict(int)
        while start <= n2-n1:
            for char in s2[start:start+n1]:
                if char not in m2:
                    m2[char]=1
                else:
                    m2[char]+=1
            if m1 == m2:
                return True
            m2.clear()
            start+=1
        return False

        