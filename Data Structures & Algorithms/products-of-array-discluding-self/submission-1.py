class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        allprod = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                allprod *= num
            if num == 0:
                zeroCount+=1
                if zeroCount >1:
                    allprod = 0
                    break
        

        output = []

        for num in nums:
            if num != 0 and zeroCount == 0:
                output.append(int(allprod/num))
            elif num == 0:
                output.append(int(allprod))
            else:
                output.append(0)

        return output
        