class Solution:
    def decodeString(self, s: str) -> str:
        
        n_s = []
        s_s = []
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            
            elif ch == '[':
                n_s.append(num)
                num = 0
                s_s.append("")
            
            elif ch!=']':
                if not n_s:
                    s_s.append(ch)
                else:
                    s_s[-1] += ch
            
            else:
                st = s_s.pop()
                nu = n_s.pop()
                if s_s:
                    s_s[-1] += st*nu
                else:
                    s_s.append(st*nu)
        
        return "".join(s_s)