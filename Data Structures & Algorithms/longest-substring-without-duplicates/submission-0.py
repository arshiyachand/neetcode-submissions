class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newstring = ""
        liststrings = []
        indexnew = 0
        for i in s:
            if i in newstring:
                liststrings.append(newstring)
                indexnew = newstring.index(i)
                #print(indexnew)
                newstring = newstring[indexnew+1:]
                #print(newstring)
                #newstring = ""
                
                newstring += i
            else:
                newstring += i
        liststrings.append(newstring)
        print(liststrings)
        print(len(str(max(liststrings, key = len))))
        return len(max(liststrings, key = len))
        