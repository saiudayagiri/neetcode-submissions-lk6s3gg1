class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for detail in details:
            if detail[11:13] > "60":
                cnt += 1
        return cnt
        