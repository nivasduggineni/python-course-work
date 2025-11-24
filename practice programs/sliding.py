arr = [2,1,5,1,3,2]
k=3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range (k,len(arr)):
    window_sum+=arr[i]-arr[i-k]
    max_sum = max(max_sum , window_sum)
print("max sum:",max_sum)


s ="abciiidef"
k=3
vowels = "aeiou"
count = 0
for i in range(k):
    if s[i] in vowels:
        count+=1
max_count = count

for i in range(k,len(s)):
    if s[i] in vowels:
        count+=1
    if s[i-k] in vowels:
        count -=1
    max_count=max(max_count,count)
print("max vowels:",max_count)


s = "abcabcbb"
seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left +=1
    seen.add(s[right])
    max_len = max(max_len,right-left+1)
print("longest substring:",max_len)



arr = [2,3,1,2,4,3]
target = 7
left = 0
window_sum = 0
min_len = float('inf')

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= target:
        min_len = min(min_len, right - left + 1)
        window_sum -= arr[left]
        left += 1

print(min_len)


s = "eceba"
k = 2
left = 0
freq = {}
max_len = 0
for right in range(len(s)):
    freq[s[right]] = freq.get(s[right],0)+1

    while len(freq)>k:
        freq[s[left]] -=1
        if freq[s[left]] == 0:
            del freq[s[left]]
        left+=1
    max_len  = max(max_len , right - left + 1)
print(max_len)
    




