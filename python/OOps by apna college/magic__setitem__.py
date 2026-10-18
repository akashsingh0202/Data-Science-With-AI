class Numbers:
    def __init__(self, values):
        self.values = values

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

nums = Numbers([10, 20, 30])

nums[1] = 99

print(nums[1])
print(nums.values)