# c = [0, 0, 1, 0, 0, 1, 0]

# c = [0, 0, 0, 0, 1, 0]

c = [0, 0, 0, 1, 0, 0]

# c = [0, 0]

def jumpingOnClouds(c):
  jumps = 0
  i = 0
  
  while i < (len(c)-1):
    if(i < (len(c)-2) and c[i+2] == 0):
      i +=1
    
    i +=1    
    jumps +=1

  return jumps


print(jumpingOnClouds(c))


# https://www.hackerrank.com/challenges/jumping-on-the-clouds
