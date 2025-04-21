nums =[1,2,3,13,2,4,5,4]

def number(nums):
	return {char : nums.count(char) for char in nums}
print(nums)