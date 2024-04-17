import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def __len__(self):
        return len(self.heap)

# Example usage:
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)

print("Priority Queue Length:", len(pq))  # Output: 3

print("Pop Task:", pq.pop())  # Output: "Task 2" (Priority 1)
print("Pop Task:", pq.pop())  # Output: "Task 3" (Priority 2)
print("Pop Task:", pq.pop())  # Output: "Task 1" (Priority 3)
