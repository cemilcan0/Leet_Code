class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""

        if len(word1)== len(word2):
            for i,j in zip(list(word1),list(word2)):
                word+=i
                word+=j
            return word
        else:
            if len(word1)>len(word2):
                for i,j in zip(list(word1)[0:len(word2)],list(word2)):
                    word+=i
                    word+=j
                word+=word1[len(word2):]
                return word
            elif len(word1)<len(word2):
                for i,j in zip(list(word1),list(word2)[:len(word1)]):
                    word+=i
                    word+=j
                word+=word2[len(word1):]
                return word
        