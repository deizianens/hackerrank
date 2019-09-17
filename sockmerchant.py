n = 10;
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3];

def sockMerchant(n, ar):
  h = {}
  result = 0

  for i in range(n):
    h[str(ar[i])] = 0

  for i in range(n):
    h[str(ar[i])] += 1
  
  for i in range(len(h)):
    result += int((h.popitem()[1]) / 2)

  return result

print(sockMerchant(n, ar))

# https://www.hackerrank.com/challenges/sock-merchant/problem
