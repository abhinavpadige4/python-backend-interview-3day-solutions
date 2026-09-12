"""
LeetCode Problem 206: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity: O(n) - Single pass through the list
Space Complexity: O(1) - Constant extra space (iterative) or O(n) for recursive call stack
"""

from typing import Optional

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_temp = current.next
        # Reverse current node's pointer
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_temp
    
    return prev

def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list recursively.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - due to recursion stack
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    # Put current node at the end
    head.next.next = head
    head.next = None
    
    return new_head

# Helper functions for testing
def create_linked_list(values: list) -> Optional[ListNode]:
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed_head1 = reverse_list(head1)
    print(f"Input: [1,2,3,4,5]")
    print(f"Output: {linked_list_to_list(reversed_head1)}")  # Expected: [5,4,3,2,1]
    print()
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    reversed_head2 = reverse_list(head2)
    print(f"Input: [1,2]")
    print(f"Output: {linked_list_to_list(reversed_head2)}")  # Expected: [2,1]
    print()
    
    # Test case 3
    head3 = create_linked_list([])
    reversed_head3 = reverse_list(head3)
    print(f"Input: []")
    print(f"Output: {linked_list_to_list(reversed_head3)}")  # Expected: []
    print()
    
    # Test recursive version
    head4 = create_linked_list([1, 2, 3, 4, 5])
    reversed_head4 = reverse_list_recursive(head4)
    print(f"Recursive - Input: [1,2,3,4,5]")
    print(f"Recursive - Output: {linked_list_to_list(reversed_head4)}")  # Expected: [5,4,3,2,1]