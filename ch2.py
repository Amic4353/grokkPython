def findSmallest(arr):
  curr_smallest = arr[0]
  smallest_indx = 0
  for i in range(1, len(arr)):
    if arr[i] < curr_smallest:
      curr_smallest = arr[i]
      smallest_indx = i
  return smallest_indx

def smallestSort(arr):
  sorted_arr = []
  for i in range(len(arr)):
    smallest_found = findSmallest(arr)
    sorted_arr.append(arr.pop(smallest_found))
  return sorted_arr

print (smallestSort([9,4,5,2,7]))
