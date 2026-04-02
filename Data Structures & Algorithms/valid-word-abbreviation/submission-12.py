class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l=0
        r=0
        while r<len(abbr):
            if l<len(word) and word[l]==abbr[r]:
                l+=1
                r+=1
            elif "a"<=abbr[r]<="z":
                return False
            else:
                if abbr[r]=="0":
                    return False
                num=0
                i=r
                while i<len(abbr) and not "a"<=abbr[i]<="z" :
                    num=num*10+int(abbr[i])
                    i+=1
                l+=num
                r=i
        return l==len(word)
        