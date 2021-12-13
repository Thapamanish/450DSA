# Question: minimum swap required to sort an array. 

# Time complexity: O(nlogn)
                  
# Auxiliary Space: O(n)

# intution : sort the array to track if swapped or not and keep a hashmap to 
            # keep the track of the index


def minSwap(arr, n):
     
    ans = 0
    temp = arr[:]
 
    # Dictionary which stores the
      # indexes of the input array
    h = {}
 
    temp.sort()
 
    for i in range(n):
         
        #h.[arr[i]
        h[arr[i]] = i
         
    init = 0
     
    for i in range(n):

        # This is checking whether
        # the current element is
        # at the right place or not
        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]
 
            # If not, swap this element
              # with the index of the
              # element which should come here
            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
 
            # Update the indexes in
              # the hashmap accordingly
            h[init] = h[temp[i]]
            h[temp[i]] = i
             
    return ans
 
# Driver code
a = [1,3,2]
n = len(a)

print(minSwap(a, n))
