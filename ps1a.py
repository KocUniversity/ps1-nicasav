n, B = list(map(int, input().strip().split()))
T = 0

# your code here
#Brute-Force Search 
result = 0
#Calculating for T = 1
for i in range(1, n + 1):
  if i % 2 ==0:
    p = 2 ** i + 1
  else:
    p = 3 ** i + 1
  result += p ** (n - i)
#Calculates for every T
while T < 10000:
  T += 1
  if result * T >B:
    break

if T == 10000 and result * T >B:
  T = 10000
if T == 10000 and result * T <B:
  T = -1
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)