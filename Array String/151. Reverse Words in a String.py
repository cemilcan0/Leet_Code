class Solution:
    def reverseWords(self, s: str) -> str:
        word=""

        a=s.split()
        a.reverse()

        for i in a:
            word+=f'{i} '
        return word.rstrip()

       
