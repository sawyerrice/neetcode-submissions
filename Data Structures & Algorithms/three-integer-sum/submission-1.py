class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)-2):
            l= i+1
            r = len(nums)-1
            pivot = nums[i]

            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            while l < r:
                if l != i+1:
                    if nums[l] == nums[l-1]:
                        l+=1
                        continue
                
                if r != len(nums)-1:
                    if nums[r] == nums[r+1]:
                        r-=1
                        continue

                if nums[l] + nums[r] == -1*pivot:
                    out.append([pivot, nums[l], nums[r]])
                    r-=1
                    l+=1
                elif nums[l] + nums[r] > -1*pivot:
                    r-=1
                else:
                    l+=1
        


        return out