class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        while i<len(abbr) and j<len(word):
            if "a"<=abbr[i]<="z":
                if word[j]!=abbr[i]:
                    return False
                i+=1
                j+=1
            else:
                if abbr[i] == "0":
                    return False
                
                # extract full number
                num = 0
                while i < len(abbr) and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                
                j += num  # skip characters in word
        
        return j == len(word) and i == len(abbr)
            
            

