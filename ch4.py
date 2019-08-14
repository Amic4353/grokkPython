def sum(arr):
  total = 0
  for x in arr:
    total+=x
  return total

def sumRec(arr, total=0):
  if arr != []:
    total+=arr.pop()
    return sumRec(arr,total)
  return total

def numberOfTasks(arr, totalTask):
  if arr == []:
    return totalTask
  else:
    totalTask+=1
    arr.pop()
    return numberOfTasks(arr, totalTask)

# find max number in a list with divide and conquer
# sort it... then just return the last number

def maxNumFunc(arr, maxNum):
  if arr == []:
    return maxNum
  else:
    if arr[0] > maxNum:
      maxNum = arr[0]
    del arr[0]
    return maxNumFunc(arr, maxNum)

# using recursion to execute binary search

def recurBinarySearch(arr,target):
  if arr == []:
    return None
  else: 
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    guess = arr[mid]
    if target == guess:
      return "true"
    if len(arr) == 1:
      del arr[0]
    if guess < target:
      arr = arr[mid+1:len(arr)]
      print("in guess<targ", arr)
    if guess > target: 
      arr = arr[0:mid]
      print("in guess>targ",arr)
    return recurBinarySearch(arr,target)

#Quick Sort
def quicksort(arr):
  if len(arr) < 2:
    return arr
  else: 
    mid=len(arr)//2
    pivot= arr[mid]
    del arr[mid]
    less = [i for i in arr if i <= pivot]
    greater = [i for i in arr if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 8,100, 78, 43,2,3,7]))

def printEachElem(arr):
  for elem in arr:
    print(elem)
  return 'done!'
# 
# O(n) -> you have to go through the entire array to execute the desired result

def doubleEachElem(arr):
  doubleElem = []
  for elem in arr:
    doubleElem.append(elem*2)
  return doubleElem
# print(doubleEachElem([1,2,3,4]))

# O(n) -> you have to go through the entire array to execute the desired result

def doubleFirstElem(arr):
  arr[0] = arr[0]*2
  return arr
# print(doubleFirstElem([1,2,3,4]))
#O(1) - constant time because it is just calling the first element and multiplying it

def multiTable(arr):
  table = [arr]
  tableNums = [2,3,7]
  for multiple in tableNums:
    currTable = []
    for elem in arr:
      currTable.append(multiple*elem)
    table.append(currTable)
    currTable = []
  return table
# print(multiTable([1,2,3,4,5]))
#O(n^2) or really 0(tableNums.length * arr.length) because you have to go through the all the multiples and appy it to all of the elems in the given array

