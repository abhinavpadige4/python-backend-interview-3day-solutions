"""
LeetCode Problem 347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Time Complexity: O(n + k log n) - O(n) for counting, O(k log n) for heap operations
Space Complexity: O(n) - For frequency map and heap
Alternative: O(n) using bucket sort
"""

from typing import List
import heapq
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using a min-heap.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Use min-heap to keep track of k most frequent elements
    # We store (-frequency, element) to simulate max-heap behavior
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # Keep heap size at most k
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract elements from heap
    return [num for freq, num in min_heap]

def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using bucket sort.
    
    Time Complexity: O(n) - Linear time
    Space Complexity: O(n) - For frequency map and buckets
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Create buckets where index = frequency
    # Maximum frequency can be len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Place elements in buckets based on frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect top k frequent elements from highest frequency buckets
    result = []
    for freq in range(len(buckets) - 1, 0, -1):  # From high to low frequency
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

def top_k_frequent_sorting(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements by sorting.
    
    Time Complexity: O(n log n) - For sorting
    Space Complexity: O(n) - For frequency map
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Sort by frequency (descending) and return top k
    sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Heap Output: {top_k_frequent(nums1, k1)}")  # Expected: [1, 2] or [2, 1]
    print(f"Bucket Sort Output: {top_k_frequent_bucket_sort(nums1, k1)}")  # Expected: [1, 2] or [2, 1]
    print(f"Sorting Output: {top_k_frequent_sorting(nums1, k1)}")  # Expected: [1, 2] or [2, 1]
    print()
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Heap Output: {top_k_frequent(nums2, k2)}")  # Expected: [1]
    print(f"Bucket Sort Output: {top_k_frequent_bucket_sort(nums2, k2)}")  # Expected: [1]
    print(f"Sorting Output: {top_k_frequent_sorting(nums2, k2)}")  # Expected: [1]
    print()
    
    # Test case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Heap Output: {top_k_frequent(nums3, k3)}")  # Expected: [-1, 2] or [2, -1]
    print(f"Bucket Sort Output: {top_k_frequent_bucket_sort(nums3, k3)}")  # Expected: [-1, 2] or [2, -1]
    print(f"Sorting Output: {top_k_frequent_sorting(nums3, k3)}")  # Expected: [-1, 2] or [2, -1]
    print()
    
    # Test case 4 - All same frequency
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Heap Output: {top_k_frequent(nums4, k4)}")  # Expected: any 3 elements
    print(f"Bucket Sort Output: {top_k_frequent_bucket_sort(nums4, k4)}")  # Expected: any 3 elements
    print(f"Sorting Output: {top_k_frequent_sorting(nums4, k4)}")  # Expected: any 3 elements