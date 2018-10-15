class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        i = int(s[::-1]) if "-" not in s else int("-{}".format(s[1:len(s)][::-1]))
        return i if i in range(-2 ** 31, 2 ** 31 - 1) else 0


so = Solution()
i = -456
print(so.reverse(i))
