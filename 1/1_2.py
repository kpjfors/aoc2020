def main(nums):
    nums = list(map(int, nums))
    nums.sort()
    solutions = dict()
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    return i * j * k


if __name__ == "__main__":
    f = open("inp1_1.txt", "r")
    nums = f.readlines()
    print(main(nums))
