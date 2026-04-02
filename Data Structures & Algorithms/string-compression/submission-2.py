class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        p = 0
        while i < len(chars):
            char = chars[i]
            j = i
            while j < len(chars) and chars[j] == char:
                j += 1
            if p < len(chars):
                chars[p] = char
            p += 1
            if j - i > 1:
                res = str(j-i)
                for cha in res:
                    chars[p] = cha
                    p+=1
            i = j
        return p
                

        