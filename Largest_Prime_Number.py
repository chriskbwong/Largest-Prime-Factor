'''
prompt:
The prime factors of 13195 are 5, 7, 13 and 29. Thus, the largest prime factor of 13195 is 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime(n):
  div_count = 0 
  factor = 1
  if n <= 1:
    return False
  while div_count < 2: 
    if n % factor == 0:
      div_count += 1
      factor += 1
    else:
      factor += 1
  if n == (factor - 1):
    return True
  else:
    return False

def LPF(num):
  if prime(num):
    return num
  factor = num - 1
  while factor > 1:
    if num % factor == 0:
      if prime(factor) == True:
        return factor
      else:
        factor -= 1
    else:
      factor -= 1
  
print(LPF(13195))
