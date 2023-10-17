# Problem link: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# 2535. Difference Between Element Sum and Digit Sum of an Array
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumElements = sum(nums)
        sumDigits = []
        for element in nums:
            Localsum = 0
            for digit in str(element):
                Localsum += int(digit)
            sumDigits.append(Localsum)
        difference = abs(sumElements - sum(sumDigits))
        return difference
