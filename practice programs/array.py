nums = [2,7,11,15]
target = 9
seen = {}
for i ,num in enumerate(nums):
    need = target - num
    if need in seen:
        print([seen[need],i])
        break
    seen[num] = i


s = "swiss"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print("Unique:", ch)
        break

s = "listen"
t = "silent"

print(sorted(s) == sorted(t))

