def prefix_sum(a):
    n = len(a)
    for i in range(1, n):
        a[i] += a[i - 1]
    return a
lst=list(map(int,input().split()))
p_sum= prefix_sum(lst)
print(p_sum)