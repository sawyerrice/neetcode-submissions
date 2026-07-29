class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        encoded += str(len(strs)) + "."
        for str1 in strs:
            encoded += str(len(str1)) + "."
        
        for str1 in strs:
            encoded += str1
                    

        return encoded


    def decode(self, s: str) -> List[str]:

        start_lens = 0
        for i in range(len(s)):
            if s[i] == ".":
                numStrs = int(s[0:i])
                start_lens = i+1
                break

        lengths = []
        ctr = start_lens
        start = ctr
        while len(lengths) < numStrs:
            if s[ctr] == ".":
                lengths.append(int(s[start:ctr]))
                start = ctr+1


            ctr+=1



        output = []
        startIdx = ctr
        for length in lengths:
            output.append(s[startIdx:startIdx+length])
            startIdx+=length
        return output


