class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 2):
            try:
                if nums[i + 1] == nums[i]:
                    count = 1
                    x = i + 2
                    try:
                        while nums[x] == nums[i]:
                            nums.remove(nums[x])
                    except:
                        continue
                else:
                    continue
            except:
                continue
        return len(nums)
                
