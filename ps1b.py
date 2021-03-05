n, B = list(map(int, input().strip().split()))
T = 0

# your code here
i = 0
result_small = 0
t = 1
T = 10000
for i in range(1, n + 1):
  if i % 2 == 0:
    p = 2 ** i + 1
  else:
    p = 3 ** i + 1
  result_small += p ** (n - i)
result_big = result_small * 10000
if result_big < B:
  T = -1
if result_small > B:
  T = 1
else:
  while i < 10000:
    t_temporary = (t + T) // 2
    if t_temporary == t or t_temporary == T:
      break
    temp_result = result_small * t_temporary
    if temp_result > B:
      T = t_temporary
    else:
      t = t_temporary
    i += 1
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)