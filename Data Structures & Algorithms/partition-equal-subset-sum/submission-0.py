class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        num_set = set()
        num_set.add(0)

        for i in range(len(nums) -1, -1, -1):
            num_set1 = set()
            for num in num_set:
                if (num + nums[i]) == target:
                    return True
                num_set1.add(num + nums[i])
                num_set1.add(num)

            num_set = num_set1

        return False