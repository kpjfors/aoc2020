def main(nums):
    nums = list(map(int,nums))
    nums.sort()
    i = 0
    j = 1
    while nums[i]+nums[j] != 2020:
        j += 1
        if j == len(nums)-1:
            i = i+1
            j = i+1
    return nums[i] * nums[j]






if __name__ == "__main__":
    f = open("inp1_1.txt", "r")
    nums = f.readlines()
    print(main(nums))