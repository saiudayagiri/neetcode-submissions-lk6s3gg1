class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        while i<len(word) and j<len(abbr):
            if abbr[j]=="0":
                return False
            if word[i]==abbr[j]:
                i+=1
                j+=1
            elif ord("a")<=ord(abbr[j])<=ord("z") or ord("A")<=ord(abbr[j])<=ord("Z"):
                return False
            else:
                num=0
                while j<len(abbr) and ord("0")<=ord(abbr[j])<=ord("9"):
                    num=num*10+int(abbr[j])
                    j+=1
                i+=num
        return i==len(word) and j==len(abbr)


        

        
        