#TC: O(m) where m is the len of the string
#SC: O(1) because we have just 26 unique characters in the hashmap


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashS = {}
        hashT = {}
        
        for i in range(len(s)):
            
            if s[i] not in hashS:
                hashS[s[i]] = t[i]
            else:
                if t[i] != hashS[s[i]]:
                    return False
            
            if t[i] not in hashT:
                hashT[t[i]] = s[i]
            else:
                if s[i] != hashT[t[i]]:
                    return False
        
        return True
            
            