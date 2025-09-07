class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}  # <str, int>
        maxLen = 1
        curLen = 1
        i = 0
        seen[s[i]] = 1
        curLeeway = k
        while i < len(s):
            repeatingChar = s[i]  # = C
            # go until we run into a problem
            right = i + curLen
            while right < len(s):
                print("i: " + str(i) + " right: " + str(right) + " curLen: " + str(curLen) + " curLeeway: " + str(curLeeway))
                if repeatingChar != s[right]:
                    curLeeway -= 1
                curLen += 1
                right += 1
                
                if curLeeway < 0:
                    curLen -= 1
                    i += 1
                    maxLen = max(maxLen, curLen)
                    break
                else:
                    maxLen = max(maxLen, curLen)
            # This next line was improperly indented - it should be part of the outer while loop
            if right == len(s):
                break
        return maxLen


# test cases:
# print(Solution().characterReplacement("ABAB", 2)) # 4
print(Solution().characterReplacement("AAABABB", 1)) # 5
assert Solution().characterReplacement("ABAB", 2) == 4
assert Solution().characterReplacement("AAABABB", 1) == 5
