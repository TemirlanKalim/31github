class NumArray:
    def __init__(self, nums):
        # Initialize an array to store cumulative sums
        self.cumulative_sums = [0] * (len(nums) + 1)

        # Compute cumulative sums
        for i in range(len(nums)):
            self.cumulative_sums[i + 1] = self.cumulative_sums[i] + nums[i]

    def sumRange(self, left, right):
        # Calculate the sum between indices left and right using cumulative sums
        return self.cumulative_sums[right + 1] - self.cumulative_sums[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
