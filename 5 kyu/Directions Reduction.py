def dirReduc(arr):
    b = len(arr)
    arr =' '.join(arr)
    for a in range(1, b): 
      arr = arr.replace("NORTH SOUTH",'')
      arr = arr.replace("SOUTH NORTH",'')
      arr = arr.replace("WEST EAST",'')
      arr = arr.replace("EAST WEST",'')
      arr = arr.split()
      arr =' '.join(arr)
    if len(arr)<2:
      arr = []
    elif len(arr) == 4:
      c = []
      c.append(arr)
      arr = c
    else:
      arr = arr.split()
            
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))