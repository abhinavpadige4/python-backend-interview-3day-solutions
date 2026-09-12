"""
LeetCode Problem 57: Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Time Complexity: O(n) - Single pass through intervals
Space Complexity: O(n) - For the result list
"""

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Insert and merge a new interval into a list of non-overlapping intervals.
    
    Args:
        intervals: List of non-overlapping intervals sorted by start time
        newInterval: New interval to insert
        
    Returns:
        List of merged non-overlapping intervals
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    # Add the merged newInterval
    result.append(newInterval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    print(f"Input: intervals = {intervals1}, newInterval = {newInterval1}")
    print(f"Output: {insert(intervals1, newInterval1)}")  # Expected: [[1,5],[6,9]]
    print()
    
    # Test case 2
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    print(f"Input: intervals = {intervals2}, newInterval = {newInterval2}")
    print(f"Output: {insert(intervals2, newInterval2)}")  # Expected: [[1,2],[3,10],[12,16]]
    print()
    
    # Test case 3 - Insert at beginning
    intervals3 = [[3,5],[6,9]]
    newInterval3 = [1,2]
    print(f"Input: intervals = {intervals3}, newInterval = {newInterval3}")
    print(f"Output: {insert(intervals3, newInterval3)}")  # Expected: [[1,2],[3,5],[6,9]]
    print()
    
    # Test case 4 - Insert at end
    intervals4 = [[1,2],[3,5]]
    newInterval4 = [6,8]
    print(f"Input: intervals = {intervals4}, newInterval = {newInterval4}")
    print(f"Output: {insert(intervals4, newInterval4)}")  # Expected: [[1,2],[3,5],[6,8]]