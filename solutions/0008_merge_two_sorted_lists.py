"""
LeetCode Problem 21: Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Time Complexity: O(n + m) - Where n and m are lengths of the two lists
Space Complexity: O(1) - Iterative approach uses constant space
"""

from typing import Optional

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Dummy node to serve as the start of the result list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining elements
    current.next = list1 if list1 else list2
    
    return dummy.next

def merge_two_lists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists recursively.
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m) - due to recursion stack
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case
    if list1.val < list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2

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
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [1,1,2,3,4,4]
    print()
    
    # Test case 2
    list3 = create_linked_list([])
    list4 = create_linked_list([])
    merged2 = merge_two_lists(list3, list4)
    print(f"Input: list1 = [], list2 = []")
    print(f"Output: {linked_list_to_list(merged2)}")  # Expected: []
    print()
    
    # Test case 3
    list5 = create_linked_list([])
    list6 = create_linked_list([0])
    merged3 = merge_two_lists(list5, list6)
    print(f"Input: list1 = [], list2 = [0]")
    print(f"Output: {linked_list_to_list(merged3)}")  # Expected: [0]
    print()
    
    # Test recursive version
    list7 = create_linked_list([1, 2, 4])
    list8 = create_linked_list([1, 3, 4])
    merged4 = merge_two_lists_recursive(list7, list8)
    print(f"Recursive - Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"Recursive - Output: {linked_list_to_list(merged4)}")  # Expected: [1,1,2,3,4,4]