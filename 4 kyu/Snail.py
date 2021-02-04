def snail(array):
    
    result = []
    while array != []:
      result += array[0]
      array.remove(array[0])
    
      if array == []: break
    
      matrix = [array[x][-1] for x in range(len(array))]
      result += matrix
      for x in range(len(array)): basket = array[x].pop(-1)
    
      matrix = array[-1]
      matrix.reverse()
      result += matrix
      array.remove(array[-1])  
    
      matrix = [array[x][0] for x in range(len(array))]
      matrix.reverse()
      result += matrix
      for x in range(len(array)): array[x].remove(array[x][0])
        
    return result


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))