class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_sub = 0

        l = 0
        r = 0
        cur_sub = 0
        while(r < len(s)):
            if s[r] not in map or map[s[r]] < l:
                map[s[r]] = r
                cur_sub+=1
            else:
                max_sub = max(cur_sub, max_sub)
                cur_sub = cur_sub - (map[s[r]] -l)

                l = map[s[r]]+1
                map[s[r]] = r
            r+=1

        return max(max_sub, cur_sub)

                
