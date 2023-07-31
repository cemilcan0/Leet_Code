class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        from math import gcd
        return str2[:gcd(len(str1),len(str2))]
    
a=Solution()
str1="ABC"
str2="ABCABC"

print(a.gcdOfStrings(str1,str2))