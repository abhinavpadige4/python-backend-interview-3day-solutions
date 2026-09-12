"""
LeetCode Problem 138: Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

Time Complexity: O(n) - Three passes through the list
Space Complexity: O(n) - Hash map to store old->new node mappings
"""

from typing import Optional

class Node:
    """Definition for a Node with random pointer."""
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """
    Create a deep copy of a linked list with random pointers.
    
    Approach:
    1. First pass: Create copy of each node and map original -> copy
    2. Second pass: Assign next and random pointers for copy nodes
    
    Args:
        head: Head of the original linked list
        
    Returns:
        Head of the copied linked list
    """
    if not head:
        return None
    
    # Step 1: Create copy of each node and map original -> copy
    old_to_new = {}
    current = head
    while current:
        copy = Node(current.val)
        old_to_new[current] = copy
        current = current.next
    
    # Step 2: Assign next and random pointers for copy nodes
    current = head
    while current:
        copy = old_to_new[current]
        copy.next = old_to_new.get(current.next)
        copy.random = old_to_new.get(current.random)
        current = current.next
    
    return old_to_new[head]

# Alternative O(1) space approach (interweaving nodes)
def copy_random_list_constant_space(head: Optional[Node]) -> Optional[Node]:
    """
    Create a deep copy using O(1) extra space (excluding output).
    
    Approach:
    1. Interweave copied nodes with original nodes
    2. Assign random pointers for copied nodes
    3. Separate the interweaved list
    
    Time Complexity: O(n)
    Space Complexity: O(1) - excluding output space
    
    Args:
        head: Head of the original linked list
        
    Returns:
        Head of the copied linked list
    """
    if not head:
        return None
    
    # Step 1: Interweave copied nodes with original nodes
    # Original: A -> B -> C
    # After:    A -> A' -> B -> B' -> C -> C'
    current = head
    while current:
        copy = Node(current.val)
        copy.next = current.next
        current.next = copy
        current = copy.next
    
    # Step 2: Assign random pointers for copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the interweaved list
    current = head
    copy_head = head.next
    while current:
        copy = current.next
        current.next = copy.next
        current = current.next
        if copy.next:
            copy.next = copy.next.next
    
    return copy_head

# Helper functions for testing
def create_random_linked_list(values: list, random_indices: list) -> Optional[Node]:
    """
    Create a linked list with random pointers for testing.
    
    Args:
        values: List of node values
        random_indices: List of indices where random pointers point to (-1 for null)
        
    Returns:
        Head of the linked list with random pointers
    """
    if not values:
        return None
    
    # Create nodes
    nodes = [Node(val) for val in values]
    
    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for i, rand_idx in enumerate(random_indices):
        if rand_idx != -1:
            nodes[i].random = nodes[rand_idx]
    
    return nodes[0] if nodes else None

def get_random_linked_list_values(head: Optional[Node]) -> tuple:
    """
    Extract values and random pointer indices from a linked list with random pointers.
    
    Returns:
        Tuple of (values_list, random_indices_list)
    """
    if not head:
        return [], []
    
    # First, map nodes to indices
    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1
    
    # Extract values and random indices
    values = []
    random_indices = []
    current = head
    while current:
        values.append(current.val)
        if current.random:
            random_indices.append(node_to_index[current.random])
        else:
            random_indices.append(-1)
        current = current.next
    
    return values, random_indices

# Test cases
if __name__ == "__main__":
    # Test case 1
    # List: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # Format: [value, random_index] where random_index points to node at that index
    head1 = create_random_linked_list([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
    copied_head1 = copy_random_list(head1)
    values1, random_indices1 = get_random_linked_list_values(copied_head1)
    print(f"Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]")
    print(f"Output: {list(zip(values1, random_indices1))}")  # Expected: same as input
    print()
    
    # Test case 2
    head2 = create_random_linked_list([1, 2], [1, -1])
    copied_head2 = copy_random_list(head2)
    values2, random_indices2 = get_random_linked_list_values(copied_head2)
    print(f"Input: [[1,2],[2,null]]")
    print(f"Output: {list(zip(values2, random_indices2))}")  # Expected: same as input
    print()
    
    # Test case 3 - Empty list
    head3 = create_random_linked_list([], [])
    copied_head3 = copy_random_list(head3)
    values3, random_indices3 = get_random_linked_list_values(copied_head3)
    print(f"Input: []")
    print(f"Output: {list(zip(values3, random_indices3))}")  # Expected: []
    print()
    
    # Test constant space version
    head4 = create_random_linked_list([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
    copied_head4 = copy_random_list_constant_space(head4)
    values4, random_indices4 = get_random_linked_list_values(copied_head4)
    print(f"Constant Space - Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]")
    print(f"Constant Space - Output: {list(zip(values4, random_indices4))}")  # Expected: same as input