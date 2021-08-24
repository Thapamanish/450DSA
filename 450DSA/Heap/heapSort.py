# Time complexity of heapify is O(Logn). 
# Time complexity of createAndBuildHeap()is O(n) and 
# the overall time complexity of Heap Sort is O(nLogn).


def heapify(heap, curr, n):
    largest = curr
    l = 2 * curr + 1
    r = 2 * curr + 2


    if l < n and heap[l] > heap[largest]:
        largest = l
    if r < n and heap[r] > heap[largest]:
        largest = r


    if largest != curr:
        heap[curr], heap[largest] = heap[largest], heap[curr]

        heapify(heap, largest, n)



def heapSort(heap):
    n = len(heap)

    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, i, n)


    for i in range(n - 1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]

        heapify(heap, 0, i)




heap = [12, 11, 13, 5, 6, 7]
heapSort(heap)
print(*heap)

