# https://leetcode.com/problems/distribute-candies-to-people/

def distributeCandies(candies, numPeople):

    loop = 0
    cnt = 0
    people = [0] * numPeople

    while candies > 0:

        if cnt == numPeople:
            cnt = 0
            loop += 1

        currentCandies = loop * numPeople + cnt + 1

        if candies - currentCandies < 0:
            people[cnt] += candies

        else:
            people[cnt] += currentCandies

        candies -= currentCandies
        cnt += 1

    return people
            


print(distributeCandies(2, 5))
print(distributeCandies(10, 3))
print(distributeCandies(7, 4))