class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for mail in emails:
            i=0
            name=""
            while mail[i]!="@" :
                if mail[i]=="+":
                    while mail[i]!="@":
                        i+=1
                    break
                if mail[i]==".":
                    i+=1
                    continue
                name+=mail[i]
                i+=1
            i+=1
            name+="@"
            
            while i<len(mail):
                
                name+=mail[i]
                i+=1
            res.add(name)
        return len(res)
            
            

        