candies = [2,3,5,1,3]
extraCandies = 3
liste = []
liste2 = []

max_list = max(candies)


for i in candies:
    #liste.append(i+extraCandies)

    if i+extraCandies >= max_list:

        liste.append(True)
    else:
        liste.append(False)
"""
for i in liste:
    if i >= max_list:
        liste2.append(True)
    else:
        liste2.append(False)
        """


