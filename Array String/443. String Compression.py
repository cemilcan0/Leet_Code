class Solution:
    def compress(self, chars: List[str]) -> int:

        a = chars[0]

        x = 1
        array = []

        for i in range(1,len(chars)):
            if chars[i] == a:
                x += 1    
            else:
                array.append(a)
                if x !=1:
                    array+=list(str(x))
                a = chars[i] 
                x = 1
        array.append(a)
        if x !=1:
                    array+=list(str(x))
                    
        chars[:] = array
        return len(chars)