def xor(s1, s2):
  if not len(s1) == len(s2):
    raise Exception("numeri di dimensione diversa")
  return [1 if s1[i] + s2[i] == 1 else 0 for i in range(len(s1))]

def n_way(nList):
  if len(nList)<1:
    return "Lista troppo piccola"
  res = nList[0]
  for i in range(1, len(nList)):
    res = xor(res, nList[i])
  
  print("S", res)

# es del prof
n_way([[1,0,0,0,1,1,1,0],[0,1,0,1,0,1,1,1],[1,0,1,0,1,0,1,1], [1,0,1,0,0,0,1,1]])