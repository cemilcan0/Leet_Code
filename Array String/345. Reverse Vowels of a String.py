class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ""
        vowel ="AaEeIiOoUu"
        liste_vowel = []
        count = 0

        for i in s:
            if i in vowel:
                liste_vowel.append(i)
        liste_vowel.reverse()

        for i in s:
            if i in vowel:
                result+=liste_vowel[count]
                count+=1
            else:
                result+=i
        return result
