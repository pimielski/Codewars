def recoverSecret(triplets):
  t=triplets
  l=[]
  z=0
  while len(t)>1:
    y = ''.join(t[c][d] for c in range(0,len(t)) for d in range(1, len(t[c])))
    for a in range(0,len(t)-1):
      for b in range(a+1,len(t)):
        if t[a][0]==t[b][0] and t[a][0] not in y:
          l.append(t[a][0])

    for a in range(0,len(t)):
      if l[-1] in t[a]: t[a].remove(l[-1])

    t=[a for a in t if a]
    z+=1
    l=l[:z]

  return ''.join(a for a in l)

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))