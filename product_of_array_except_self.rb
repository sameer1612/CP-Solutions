# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
  left_prods = [1]
  right_prods = [1]
  lp = 1
  rp = 1
  count = nums.size
  
  (1...count).each do |i|
    lp *= nums[i-1]
    left_prods << lp
    
    rp *= nums[count - i]
    right_prods << rp
  end
  
  (0...count).map do |i|
    left_prods[i] * right_prods[count - i -1]
  end
end
