class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for mail in emails:
            i=0
            localname=""
            while mail[i]!="@" :
                if mail[i]=="+":
                    while mail[i]!="@":
                        i+=1
                    break
                if mail[i]==".":
                    i+=1
                    continue
                localname+=mail[i]
                i+=1
            i+=1
            domainname=""
            while i<len(mail):
                
                domainname+=mail[i]
                i+=1
            res.add(localname+"@"+domainname)
        return len(res)
            
            

        