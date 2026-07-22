class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        for num in nums:
            if num in map:
                map[num] +=1
            else:
                map[num] = 1

        
        ret = sorted(map.items(), key = lambda i: i[1])

        for i in range(len(ret)):
            ret[i] = ret[i][0]

        return ret[len(ret)-k:len(ret)]