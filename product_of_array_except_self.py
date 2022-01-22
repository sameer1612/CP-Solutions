class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prods = []
        left_prods = [1]
        right_prods = [1]
        last_left_prod = 1
        last_right_prod = 1
        
        for i in range(1, n):
            last_left_prod *= nums[i - 1]
            left_prods.append(last_left_prod)

            last_right_prod *= nums[n - i]
            right_prods.append(last_right_prod)

        right_prods.reverse()

        for i in range(n):
            prods.append(left_prods[i] * right_prods[i])

        return prods


print(Solution().productExceptSelf([1, 2, 3, 4]))
