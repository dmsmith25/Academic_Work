print(1)
def allsubsets(s):
    print(1)
    # given a set s as a list, return all subsets of s
    # base case. A null set has one subset, the null set.
    if len(s) == 0:
        ans = [[]]
    else:
        a = s[0]
        n = len(s)
        rest = s[1:n]
        print(5)
        ans = allsubsets(rest)  # from proof, this is B
        n = len(ans)            # n = n - 1
        ans[:0] = ans           # ans now contains two copies of B
        i = 0
        while i < n:
            ans[i] = [a] + ans[i]
            i = i + 1

    return ans


print(allsubsets([1,2,3]))