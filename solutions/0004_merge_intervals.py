"""
LeetCode Problem 56: Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Time Complexity: O(n log n) - Sorting takes O(n log n), merging takes O(n)
Space Complexity: O(n) - For the result list (or O(1) if we modify in-place)
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    
    Args:
        intervals: List of intervals where each interval is [start, end]
        
    Returns:
        List of merged non-overlapping intervals
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # If current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge the intervals by extending the end time
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add current interval to merged list
            merged.append(current)
    
    return merged

# Test cases
if __name__ == "__main__":
    # Test case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Input: intervals = {intervals1}")
    print(f"Output: {merge(intervals1)}")  # Expected: [[1,6],[8,10],[15,18]]
    print()
    
    # Test case 2
    intervals2 = [[1,4],[4,5]]
    print(f"Input: intervals = {intervals2}")
    print(f"Output: {merge(intervals2)}")  # Expected: [[1,5]]
    print()
    
    # Test case 3 - No overlap
    intervals3 = [[1,2],[3,4],[5,6]]
    print(f"Input: intervals = {intervals3}")
    print(f"Output: {merge(intervals3)}")  # Expected: [[1,2],[3,4],[5,6]]
    print()
    
    # Test case 4 - Complete overlap
    intervals4 = [[1,4],[2,3]]
    print(f"Input: intervals = {intervals4}")
    print(f"Output: {merge(intervals4)}")  # Expected: [[1,4]]