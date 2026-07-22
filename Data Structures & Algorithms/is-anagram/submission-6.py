class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        map = {}

        if len(s) < len(t):
            first_string = s
            second = t
        else:
            first_string = t
            second = s
        for c in first_string:
            if c in map:
                map[c] +=1
            else:
                map[c] = 1

        for c in second:
            if c in map:
                if map[c] == 0:
                    return False
                elif map[c] == 1:
                    del map[c]
                else:
                    map[c] -= 1
            else:
                return False

        return True
