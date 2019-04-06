class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        a = {')': '(', ']': '[', '}': '{'}
        l = ['#']
        for i in s:
            if i in a:
                if a[i]!=l.pop():
                    return False
            else:
                l.append(i)
        return len(l) == 1











s=Solution()
print(s.isValid(r'((}'))