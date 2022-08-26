def first_last6(nums):
  for i in range(len(nums)):
    print(nums[0])
    if nums[0] == 6 or nums[-1] == 6:
      return True
    else:
      return False
      
print(first_last6())