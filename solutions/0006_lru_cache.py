"""
LeetCode Problem 146: LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity) - Stores at most capacity items
"""

class Node:
    """Doubly linked list node for LRU Cache."""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU Cache implementation using hash map and doubly linked list.
    
    Time Complexity: O(1) for get and put operations
    Space Complexity: O(capacity)
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # Map key to node
        
        # Dummy head and tail nodes for easier edge case handling
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """
        Get value of key if exists, otherwise return -1.
        Move accessed node to head (most recently used).
        
        Args:
            key: Key to lookup
            
        Returns:
            Value associated with key, or -1 if not found
        """
        if key in self.cache:
            node = self.cache[key]
            # Move to head (most recently used)
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair in cache.
        If key exists, update value and move to head.
        If cache is full, remove least recently used item before inserting.
        
        Args:
            key: Key to insert/update
            value: Value to associate with key
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Insert new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used item (before tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

# Test cases
if __name__ == "__main__":
    # Test case 1 from LeetCode example
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"get(1): {lru.get(1)}")  # returns 1
    lru.put(3, 3)                  # evicts key 2
    print(f"get(2): {lru.get(2)}")  # returns -1 (not found)
    lru.put(4, 4)                  # evicts key 1
    print(f"get(1): {lru.get(1)}")  # returns -1 (not found)
    print(f"get(3): {lru.get(3)}")  # returns 3
    print(f"get(4): {lru.get(4)}")  # returns 4
    print()
    
    # Test case 2
    lru2 = LRUCache(1)
    lru2.put(2, 1)
    print(f"get(2): {lru2.get(2)}")  # returns 1
    lru2.put(3, 2)                  # evicts key 2
    print(f"get(2): {lru2.get(2)}")  # returns -1 (not found)
    print(f"get(3): {lru2.get(3)}")  # returns 2