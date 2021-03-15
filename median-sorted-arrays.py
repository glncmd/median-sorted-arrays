def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    
    if n == 0:
        raise ValueError

    a_min, a_max, half = 0, m, (m + n + 1) / 2

    while a_min <= a_max:
        a = int((a_min + a_max) / 2)
        b = int(half - a)

        if a > 0 and nums1[a - 1] > nums2[b]:
            a_max -= 1

        elif a < m and nums2[b - 1] > nums1[a]:
            a_min += 1

        else:
            if a == 0:
                left_max = nums2[b - 1]

            elif b == 0:
                left_max = nums1[a - 1]

            else:
                left_max = max(nums1[a - 1], nums2[b - 1])

            if (m + n) % 2 == 1:
                return left_max

            if a == m:
                right_min = nums2[b]

            elif b == n:
                right_min = nums1[a]

            else:
                right_min = min(nums1[a], nums2[b])

            return (left_max + right_min) / 2