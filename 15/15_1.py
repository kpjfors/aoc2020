def main(inp):
    inp = list(map(int,inp.split(",")))
    nums = {}
    i = 0
    round = 1
    latest = 0
    said = 0
    for i in range(len(inp)):
        nums[inp[i]] = i+1
        latest = nums[inp[i]]
        round += 1

    while True:
        if not said in nums.keys():
            nextsaid = 0
        else:
            nextsaid = round - nums[said]
        nums[said] = round
        said = nextsaid
        round += 1
        if round == 2020:
            return said

if __name__ == "__main__":
    f = open("inp15_1.txt", "r")
    inp = f.read()
    print(main(inp))
