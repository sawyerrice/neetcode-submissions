class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s = s.upper()
        
        l = 0
        r = len(s)-1

        bounds = [[65,90], [97,122]]
        while  l < r:
            lvalid = False
            rvalid = False

            lchar = s[l]
            rchar = s[r]
            
            if s[l].isupper() or s[l].isdigit():
                lvalid = True
            else:
                l+=1

            if s[r].isupper() or s[r].isdigit():
                rvalid = True
            else:
                r-=1

            if lvalid and rvalid:
                if lchar != rchar:
                    return False
                l+=1
                r-=1


            
        return True
        