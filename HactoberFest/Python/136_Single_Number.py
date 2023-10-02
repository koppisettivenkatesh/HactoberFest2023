class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return nums
        temp_set = set()
        for i in nums:
            if i in temp_set:
                temp_set.remove(i)
            else:
                temp_set.add(i)
        return int(''.join(map(str, temp_set)))
