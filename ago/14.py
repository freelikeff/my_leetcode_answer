class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        lenmin = 100
        for item in strs:
            if len(item)==0:
                return ''
            if len(item) < lenmin:
                lenmin=len(item)
        ans=[]
        for i in range(0,lenmin):
            for item in strs:
                if item[i]!=strs[0][i]:
                    return ''.join(ans)
            ans.append(strs[0][i])
        if len(ans)==0: return ''
        else: return ''.join(ans)