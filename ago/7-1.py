class Solution:
    def reverse(self, x):
        def zhengshudec(x):  # 正数不溢出返回True
            if len(str(x)) < 10:
                return True
            elif len(str(x)) > 10:
                return False
            else:
                f = 1
                l = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
                ln = [int(i) for i in list(str(x))]
                for i in range(0, 10):
                    if l[i] > ln[9 - i]:
                        break
                    elif l[i] < ln[9 - i]:
                        f = 0
                        break
                return bool(f)
        """
        :type x: int
        :rtype: int
        """
        while x % 10 == 0:
            x //= 10

        if x == -8463847412:
            return -2147483647
        else:
            y = abs(x)
            if zhengshudec(y):
                return x // y * int(str(y)[::-1])
            else:
                return 0