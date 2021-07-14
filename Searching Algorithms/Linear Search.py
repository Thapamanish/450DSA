# Linear Search

def linear_search(arr, key):
   for i in range(len(arr)):
      if arr[i] == key:
         return i
   return -1




arr = list(map(int, input().split()))
key = int(input())
pos = linear_search(arr, key)
if pos != -1:
   print("Element found at position", pos + 1)
else:
   print("Element not found") 