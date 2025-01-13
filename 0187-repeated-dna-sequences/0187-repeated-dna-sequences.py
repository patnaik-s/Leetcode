class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq= set()
        rep= set()

        for i in range(len(s)-9):
            cur =s[i:i+10]
            if cur in seq:
                rep.add(cur)
            seq.add(cur)
        return list(rep)