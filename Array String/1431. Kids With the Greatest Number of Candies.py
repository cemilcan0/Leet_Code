class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        liste = []

        max_list = max(candies)


        for i in candies:
            if i+extraCandies >= max_list:

                liste.append(True)
            else:
                liste.append(False)
        return liste

        