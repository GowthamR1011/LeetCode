class Solution:
    def finalString(self, s: str) -> str:
        new_str = ""

        for c in s:
            if c != 'i':
                new_str = new_str + c
            else:
                new_str = new_str[::-1]


        return new_str