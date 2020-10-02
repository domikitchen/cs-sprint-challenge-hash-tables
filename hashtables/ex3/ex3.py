def intersection(arrays):
    """
    YOUR CODE HERE
    """
    count = 0
    dic = {}
    res = []

    while count < len(arrays):
      for i in arrays[0]:
        if i in dic:
          num = dic[i]
          dic[i] = num + 1
        
        else:
          dic[i] = 1
      arrays.append(arrays[0])
      arrays.pop(0)
      count += 1

    for i in dic:
      if dic[i] == len(arrays):
        res.append(i)
    
    
    return res

# result = intersection([
#     [1,2,3],
#     [1,4,5,3],
#     [1,6,7,3]
# ])

# print(result == [1,3])
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
