def main(inp, length):
    inp = list(map(int,inp))
    prev = [x for x in inp[:length]]
    for i in inp[length:]:
        if sumofprevious(prev,i):
            prev.pop(0)
            prev.append(i)
        else:
            return findcontagious(inp, i)

def sumofprevious(prev, goal):
    i = 0
    j = 1
    while prev[i]+prev[j] != goal:
        j += 1
        if j == len(prev):
            i = i+1
            j = i+1
        if j == len(prev):
            return False
    return True

def findcontagious(inp, goal):
    starti = 0
    while starti < len(inp):
        retsum = 0
        for i in range(starti,len(inp)-1):
            retsum += inp[i]
            if retsum == goal:
                return min(inp[starti:i])+max(inp[starti:i])
        starti += 1
    return False

if __name__ == "__main__":
    f = open("inp9_1.txt", "r")
    inp = f.readlines()
    print(main(inp, 25))