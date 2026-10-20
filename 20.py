def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4))

def show_profile(**info):
    for key , value in info.items():
        print(f"{key}: {value}")

show_profile(name="Ali", age=22)

def min_max(nums):
    return min(nums), max(nums)

low,high = min_max([3,9,1])
print(low,high)