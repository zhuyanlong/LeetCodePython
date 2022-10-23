class Solution:
    def isValid(self, s):
        stack=[0]
        for i in range(len(s)):
            if s[i]==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif s[i]==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif s[i]=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack)==1:
            return True
        else:
            return False


def main():
    s = "{[]}"
    sol=Solution()
    res=sol.isValid(s)
    print(res)

main()