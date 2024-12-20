'''Remove All Adjacent Duplicates in String II
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

'''

#SOLUTION

def removeDuplicates(self, s, k):
       
        stack = [["#",0]] # Just a place holder

        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c,1])

            
        return "".join(c*cnt for [c,cnt] in stack)