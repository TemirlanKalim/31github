class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fm, sm, tm = float('-inf'), float('-inf'), float('-inf')
        if len(set(nums))>=3:
            for i in set(nums):
                if i > fm:
                    tm = sm
                    sm = fm
                    fm = i
                elif i > sm:
                    tm = sm
                    sm = i
                elif i > tm:
                    tm = i
                else:
                    continue
        else:
            return max(nums)
        return tm
