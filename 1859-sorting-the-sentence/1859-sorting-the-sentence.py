import string
class Solution:
    def sortSentence(self, s: str) -> str:
        res = sorted(s.split(), key=lambda x: x[::-1])
        return " ".join(i.rstrip(string.digits) for i in res)
        