sum = 0
for i in range(2, 101, 2):
  sum += i
print(sum)

sum_2 = 0
for i in range(1, 101):
  if i % 2 == 0:
    sum_2 += i
print(sum_2)

input()