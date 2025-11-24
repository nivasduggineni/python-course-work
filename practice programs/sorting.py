arr = [4,2,7,1]
arr.sort()
print(arr)


arr = ["hi","hello","a"]
arr.sort(key=len)
print(arr)

pairs = [(1,3),(2,1),(4,2)]
pairs.sort(key=lambda x:x[1])
print(pairs)

coins = [25,10,5,1]
amount = 49
count = 0
for c in coins:
    while amount >=c:
        amount-=c
        count+=1
print(count)

meetings = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
meetings.sort(key = lambda X:X[1])
count =1
end_time = meetings[0][1]
for s , e  in meetings[1:]:

    if s >=end_time:
        count +=1
        end_time = e
print("max meetings:",count)



intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()

merged = [intervals[0]]

for s,e in intervals[1:]:
    last = merged[-1]
    if s <= last[1]:
        last[1] = max(last[1], e)
    else:
        merged.append([s,e])

print(merged)


points = [[10,16],[2,8],[1,6],[7,13]]
points.sort(key=lambda x: x[1])
arrows =  1
end = points[0][1]
for s,e in points[1:]:
    if s > end:
        arrows +=1
        end=e
print(arrows)


