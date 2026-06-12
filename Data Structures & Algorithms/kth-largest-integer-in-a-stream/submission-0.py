class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-(self.k)]
        
        #[1,2,4,3,5,7,8]
