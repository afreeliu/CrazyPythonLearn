

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# 思路一：暴力解法, 该解法的时间复杂度为 O(n^2), 不理想
def sum_one(nums, target):
    count = len(nums)
    if count == 0:
        return []
    for i in range(count):
        for j in range(i+1, count):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# 思路二：利用数组的顺序排序，可以转化成字典，字典的key为数组的值，字典的value为数组的下标
def sum_two(nums, target):
    num_dict = {}
    for index, value in enumerate(nums):
        num_dict[value] = index
    for i, num in enumerate(nums):
        j = num_dict.get(target - num)
        print(j)
        if j is not None and i != j:
            return [i, j]

print(sum_two([2, 7, 11, 15], 9))