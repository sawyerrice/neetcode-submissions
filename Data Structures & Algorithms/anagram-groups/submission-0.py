class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}
        for word in strs:
            word_list = list(word)
            word_list.sort()

            reorder_str = ".".join(word_list)
            if reorder_str in map:
                map[reorder_str].append(word)
            else:
                map[reorder_str] = [word]

        out = []
        for key in map.keys():
            out += [map[key]]

        print(out)
        return out
