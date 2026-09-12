"""
LeetCode Problem 215: Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Time Complexity: O(n log k) - Using min-heap of size k
Space Complexity: O(k) - For the heap
Alternative: O(n) average with QuickSelect, O(n^2) worst case
"""

import heapq
from typing import List
import random

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find the kth largest element using a min-heap.
    
    Args:
        nums: List of integers
        k: The kth position to find (1-indexed from largest)
        
    Returns:
        The kth largest element
    """
    # Use a min-heap of size k to keep track of k largest elements
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the heap is the kth largest element
    return min_heap[0]

def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    Find the kth largest element using QuickSelect algorithm.
    
    Time Complexity: O(n) average, O(n^2) worst case
    Space Complexity: O(1) - in-place partitioning
    
    Args:
        nums: List of integers
        k: The kth position to find (1-indexed from largest)
        
    Returns:
        The kth largest element
    """
    # Convert kth largest to (n-k)th smallest index
    target_index = len(nums) - k
    
    def quick_select(left: int, right: int) -> int:
        """QuickSelect helper function."""
        # Choose random pivot to avoid worst case
        pivot_index = random.randint(left, right)
        pivot_value = nums[pivot_index]
        
        # Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Partition: all elements < pivot go to left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        # Check if pivot is at target index
        if store_index == target_index:
            return nums[store_index]
        elif store_index < target_index:
            return quick_select(store_index + 1, right)
        else:
            return quick_select(left, store_index - 1)
    
    return quick_select(0, len(nums) - 1)

def find_kth_largest_sorting(nums: List[int], k: int) -> int:
    """
    Find the kth largest element by sorting.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sorting algorithm
    
    Args:
        nums: List of integers
        k: The kth position to find (1-indexed from largest)
        
    Returns:
        The kth largest element
    """
    nums.sort()
    return nums[-k]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Heap Output: {find_kth_largest(nums1, k1)}")  # Expected: 5
    print(f"QuickSelect Output: {find_kth_largest_quickselect(nums1[:], k1)}")  # Expected: 5
    print(f"Sorting Output: {find_kth_largest_sorting(nums1[:], k1)}")  # Expected: 5
    print()
    
    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Heap Output: {find_kth_largest(nums2, k2)}")  # Expected: 4
    print(f"QuickSelect Output: {find_kth_largest_quickselect(nums2[:], k2)}")  # Expected: 4
    print(f"Sorting Output: {find_kth_largest_sorting(nums2[:], k2)}")  # Expected: 4
    print()
    
    # Test case 3
    nums3 = [1]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Heap Output: {find_kth_largest(nums3, k3)}")  # Expected: 1
    print(f"QuickSelect Output: {find_kth_largest_quickselect(nums3[:], k3)}")  # Expected: 1
    print(f"Sorting Output: {find_kth_largest_sorting(nums3[:], k3)}")  # Expected: 1
    print()
    
    # Test case 4 - All same elements
    nums4 = [7, 7, 7, 7, 7]
    k4 = 3
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Heap Output: {find_kth_largest(nums4, k4)}")  # Expected: 7
    print(f"QuickSelect Output: {find_kth_largest_quickselect(nums4[:], k4)}")  # Expected: 7
    print(f"Sorting Output: {find_kth_largest_sorting(nums4[:], k4)}")  # Expected: 7