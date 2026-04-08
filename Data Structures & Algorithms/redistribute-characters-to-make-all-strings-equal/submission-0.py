class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        arr=[0]*26
        for word in words:
            for c in word:
                arr[ord(c)-ord("a")]+=1
        for num in arr:
            if num%len(words):
                return False
        return True
        