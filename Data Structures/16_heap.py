#Heap queue or heapq (or priority queue)
# In Python, heaps are implemented as min-heaps by default, meaning the smallest element is always at the root of the structure, making it efficient to access.
import heapq
l = [25, 20, 15, 30, 40]

#converting list into heap
heapq.heapify(l)

print("heap queue: ",l)#heap queue:  [15, 20, 25, 30, 40](always 1st ele is smallest)

#Using heap as max-heap
num = [10, 20, 15, 30, 45]#By default, Python’s heapq implements a min-heap. To create a max-heap, you can simply invert the values (store negative numbers).
max_heap = [-n for n in num]#inverting values
maxi = [n for n in num]
print(maxi) #[10, 20, 15, 30, 45]
heapq.heapify(max_heap)

print(max_heap)#[-45, -30, -15, -10, -20]
print("Largest element: ", -max_heap[0]) #45

#Append and Pop
#heapq.heappush(heap, item) adds a new element to the heap.
#heapq.heappop(heap) removes and returns the smallest element.
h = [10,20,15,30,40]
heapq.heapify(h)#minheap

heapq.heappush(h,5)
print(h)

min = heapq.heappop(h)
print("Smallest: ", min)
print(h)

#Appending and popping simultaneously
#eapq.heappushpop() function efficiently pushes a new element onto the heap and pops the smallest one in a single step. This is faster than doing heappush() followed by heappop() separately, as it maintains the heap structure with just one adjustment. It takes two arguments: the heap and the element to be pushed.
mini = heapq.heappushpop(h, 5)
print(mini) #5
print(h)#[10, 20, 15, 30, 40]

#Finding Largest and Smallest elements
# Python’s nlargest() and nsmallest() functions work on any iterable, not just heaps. They scan efficiently and return the requested number of largest or smallest elements.
#heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
#heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.
maximum = heapq.nlargest(3, h)#[10, 20, 15, 30, 40]
print(" 3 largest elements: ", maximum)# 3 largest elements:  [40, 30, 20]

minimum = heapq.nsmallest(3, h)
print(" 3 smallest elements: ", minimum)#3 smallest elements:  [10, 15, 20]

#replace and merge operations

#heapq.heapreplace() function is a combination of pop and push.
#It returns the smallest element before replacing it.
#It is more efficient than using heappop() followed by heappush() because it performs both operations in one step.
#heapq.merge() function is used to merge multiple sorted iterables into a single sorted heap. 
h1 = [10,20,15,30,40]
heapq.heapify(h1)

minis = heapq.heapreplace(h1,5)
print(minis)#10
print(h1)#[5, 20, 15, 30, 40]

h2 = [2,4,6,8]
h3 = list(heapq.merge(h1,h2))
print("Merged heap: ", h3)#Merged heap:  [2, 4, 5, 6, 8, 20, 15, 30, 40]
#NOTE: eapreplace() always pops smallest element and then pushes a new one whereas, heappushpop() pushes new element first, then pops smallest.
#Use heapreplace() when you always want the new element to be in the heap and heappushpop() when new element may or may not stay (depending on comparison).

#-----using functions-------
def min_heapify(h, n, i):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    #if left child exists and smaller than root
    if left < n and h[left] < h[smallest]:
        smallest = left
    #if left child exists and smaller than root
    if right < n and h[right] < h[smallest]:
        smallest = right
    #if root is not smallest,swap and continue heapifying
    if smallest !=i:
        h[i], h[smallest] = h[smallest], h[i]
        min_heapify(h, i, smallest)

def max_heapify(h, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    #if left child exists and greater than root
    if left < n and h[left] > h[largest]:
        largest = left
    #if left child exists and greater than root
    if right < n and h[right] > h[largest]:
        largest = right
    #if root is not largest,swap and continue heapifying
    if largest !=i:
        h[i], h[largest] = h[largest], h[i]
        min_heapify(h, i, largest)

hp= [3, 1, 6, 5, 2, 4]
min_heapify(hp, len(hp), 0)
print("After Min heapify:", hp)#Min heapify: [1, 3, 6, 5, 2, 4]

arr = [3, 1, 6, 5, 2, 4]
max_heapify(arr, len(arr), 0)
print("After max heapify:", arr)#Array after max-heapify at root: [6, 1, 3, 5, 2, 4]


def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, n, i)
    return arr

arr = [4, 10, 3, 5, 1]
min_heap = build_min_heap(arr)
print("Min-heap built:", min_heap)

heapsortarr = [5,3,4,7,1]
mini_heap = heapsortarr[:]
heapq.heapify(heapsortarr)
sorted_arr = [heapq.heappop(heapsortarr) for i in range(len(heapsortarr))]
print("heapsort asc order: ", sorted_arr)

max_heap = [-x for x in mini_heap]
heapq.heapify(max_heap)
sorted_desc = [-heapq.heappop(max_heap) for i in range(len(max_heap))]
print("Heapsort desc: ", sorted_desc)