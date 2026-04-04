class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            r = len(email)-1
            while email[r]!="@":
                r-=1
            second = email[r:]
            first = ""
            for char in email:
                if char==".":
                    continue
                if char =="+" or char=="@":
                    break
                first+=char
            res.add(first+second)
        return len(res)
        