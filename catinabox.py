nums = input().split(" ")
vol = int(nums[0]) * int(nums[1]) * int(nums[2])
if vol == int(nums[3]):
    print("COZY")
elif vol < int(nums[3]):
    print("TOO TIGHT")
else:
    print("SO MUCH SPACE")
