
left = []
right = []

with open("input.txt") as f:
  lines = f.readlines()
  
  for l in lines:
    nums = l.split("   ")
    left.append(int(nums[0]))
    right.append(int(nums[1]))

left.sort()
right.sort()

sum = 0
for i in range(len(left)):
  distance = abs(left[i] - right[i])
  sum += distance
print(sum)
#print(right)

## Part 2

similarity_sum = 0

for i in range(len(left)):
  count = 0
  for j in range(len(right)):
    if left[i] == right[j]:
      count += 1
  
  similarity = left[i] * count
  #print(similarity)
  similarity_sum += similarity

print("part 2", similarity_sum)