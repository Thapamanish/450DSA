
# Time complexity : O(len(s2) * alphabetSize)
# Space complexity: O(alphabetSize)

def solve(s1, s2):
    s1Length = len(s1)
    s2Length = len(s2)

    s1Hash = [0] * 26
    s2Hash = [0] * 26

    left = 0
    right = 0

    if s1Length > s2Length:
        return False

    while right < s1Length:
        s1Hash[ord(s1[right]) - ord('a')] += 1
        s2Hash[ord(s2[right]) - ord('a')] += 1
        right += 1


    right -= 1
    while right < s2Length:
  
        if s1Hash == s2Hash:
            return True

        right += 1

        if right != s2Length:
            s2Hash[ord(s2[right]) - ord('a')] += 1

        s2Hash[ord(s2[left]) - ord('a')] -= 1
        left += 1


    return False



s1 = 'onetwofour' 
s2 = 'hellofourtwooneworld' 
print(solve(s1, s2))

