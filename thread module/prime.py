def get_prime():
  result = [1,2]
  for i in range(3,101):
    for e in range(2,i):
      if i%e:
        break
      result.append(i)
  return result