class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outdict = {}
        output = []

        for item in strs:
            key = ''.join(sorted(item))
            if key in outdict:
                outdict[key].append(item)
            else:
                outdict[key] = [item]

       

        for item in outdict:
            output.append(outdict[item])
        
        return output


        