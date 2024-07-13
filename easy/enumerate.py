def enumerate(iterable, start):
  res = []
  counter = start
  for val in iterable:
    res.append((counter, val))
    counter += 1
  return res
