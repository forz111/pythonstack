import bisect

n = int(input())
line = list(map(int, input().split()))

l2 = [line[-1]]
answer = 0
for elem in reversed(line[:-1]):
    new_ind = bisect.bisect_left(l2, elem)
    answer += new_ind
    l2.insert(new_ind, elem)

print(answer)
