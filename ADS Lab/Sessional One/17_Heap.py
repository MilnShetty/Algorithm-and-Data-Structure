import heapq


max_heap = []


heapq.heappush(max_heap, 10)
heapq.heappush(max_heap, 5)
heapq.heappush(max_heap, 15)
heapq.heappush(max_heap, 7)
heapq.heappush(max_heap, 20)


print("Max Heap (before extracting max element):", max_heap)


max_element = heapq.heappop(max_heap)
print("Extracted Maximum Element:", max_element)


print("Max Heap (after extracting max element):", max_heap)


new_element = 25
heapq.heappush(max_heap, new_element)


print("Max Heap (after inserting", new_element, "):", max_heap)
