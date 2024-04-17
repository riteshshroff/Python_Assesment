class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  # Dummy head node
        self.tail = Node(None, None)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict_least_recently_used()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _evict_least_recently_used(self):
        evict_node = self.tail.prev
        self._remove_node(evict_node)
        del self.cache[evict_node.key]

# Example usage:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))  # Output: 1
print(cache.get(2))  # Output: 2

cache.put(3, 3)

print(cache.get(2))  # Output: -1 (2 was evicted)
print(cache.get(3))  # Output: 3
