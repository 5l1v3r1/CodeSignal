def makeArrayConsecutive2(statues):
    ans = 0
    for i in range(min(statues), max(statues)):
        if i not in statues:
            ans += 1

    return ans