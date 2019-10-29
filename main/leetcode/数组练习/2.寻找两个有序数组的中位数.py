'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


def findMedianSortedArrays(nums1, nums2):

    numsLeng1 = len(nums1)
    numsLeng2 = len(nums2)
    count = numsLeng1 + numsLeng2
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
    if count % 2 == 0:
        z = int(count/2 - 1)
        result = nums1[z] + nums1[z+1]
        return result/2
    else:
        z = int((count-1)/2)
        return nums1[z]



def findMedianSortedArrays_two(nums1, nums2):

    numsLeng1 = len(nums1)
    numsLeng2 = len(nums2)
    count = numsLeng1 + numsLeng2
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
    if count % 2 == 0:
        z = int(count/2 - 1)
        result = nums1[z] + nums1[z+1]
        return result/2
    else:
        z = int((count-1)/2)
        return nums1[z]


findMedianSortedArrays([1,2,7], [4,5,6])

