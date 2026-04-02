class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for log in logs :
            if log == "./":
                continue
            elif log == "../":
                cnt -= 1
                if cnt<0:
                    cnt=0
            else:
                cnt += 1
        return cnt if cnt > 0 else 0

        