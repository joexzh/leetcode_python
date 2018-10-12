class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)

        if len2 < len1:
            nums1, len1, nums2, len2 = nums2, len2, nums1, len1
        if len2 == 0:
            return 0.0

        ilo, ihi, half_len = 0, len1, (len1 + len2 + 1) // 2
        while ilo <= ihi:
            i = (ilo + ihi) // 2
            j = half_len - i
            if i < len1 and nums1[i] < nums2[j - 1]:
                ilo = i + 1
            elif i > 0 and nums2[j] < nums1[i - 1]:
                ihi = i - 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1:
                    return max_left

                if i == len1:
                    min_right = nums2[j]
                elif j == len2:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0

    def findKEleSortedArrays(self, a1: list, a2: list, k: int):
        """
        find the k'th element in two sorted arrays.
        :param k: from 1
        :param a1: array 1
        :param a2: array 2
        :return: the element
        """
        if k < 1:
            raise ValueError("k must bigger equal than 1")
        l1, l2 = len(a1), len(a2)

        if l2 < l1:
            a1, l1, a2, l2 = a2, l2, a1, l1
        if l2 == 0 or l1 + l2 < k:
            raise IndexError("len(a1)+len(a2) is less than k")
        ilo, ihi = 0, l1
        while ilo <= ihi:
            i = (ilo + ihi) // 2
            j = k - i

            if l2 < j or (i < l1 and 0 < j and a1[i] < a2[j - 1]):
                ilo = i + 1
            elif j < l2 and 0 < i and a2[j] < a1[i - 1]:
                ihi = i - 1
            else:
                if i == 0:
                    k_val = a2[j - 1]
                elif j == 0:
                    k_val = a1[i - 1]
                else:
                    k_val = max(a1[i - 1], a2[j - 1])

                return k_val


def main():
    s = Solution()
    # a = []
    # b = []
    # mid = s.findMedianSortedArrays(a, b)
    # print(mid)

    a1 = [1,2,3,4,5,6,7,8,9]
    a2 = [2]
    print(s.findKEleSortedArrays(a1, a2, 4))


if __name__ == '__main__':
    main()
