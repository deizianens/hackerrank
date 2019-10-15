n = 12
s = "DDUUDDUDUUUD"

def countingValleys(n, s):
  v = 0
  aux = 0

  for i in range(n):
    if (s[i] == 'D' and aux == 0):
      v += 1
      aux += -1
    else:
      if(s[i] == 'U'):
        aux += 1
      else:
        aux += -1
  return v


print(countingValleys(n, s))

# https://www.hackerrank.com/challenges/counting-valleys/
