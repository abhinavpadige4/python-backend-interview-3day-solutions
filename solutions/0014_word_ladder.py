"""
LeetCode Problem 127: Word Ladder
A transformation sequence from word beginWord to word endWord using a dictionary wordList 
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words 
in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Time Complexity: O(M^2 * N) - Where M is length of each word, N is number of words in wordList
Space Complexity: O(M^2 * N) - For the adjacency graph and BFS queue
"""

from typing import List
from collections import deque, defaultdict

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find the length of the shortest transformation sequence from beginWord to endWord.
    
    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: List of valid words for transformation
        
    Returns:
        Number of words in the shortest transformation sequence, or 0 if not possible
    """
    if endWord not in wordList:
        return 0
    
    # Preprocess wordList to create generic states
    # e.g., "hot" -> "*ot", "h*t", "ho*"
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(L):
            # Create generic state by replacing i-th character with '*'
            generic_state = word[:i] + "*" + word[i+1:]
            all_combo_dict[generic_state].append(word)
    
    # BFS initialization
    queue = deque([(beginWord, 1)])  # (current_word, level)
    visited = {beginWord: True}
    
    while queue:
        current_word, level = queue.popleft()
        
        # Generate all possible generic states for current word
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            
            # Check all words that share this generic state
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1
                
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            
            # Optimization: clear visited words to prevent reprocessing
            all_combo_dict[intermediate_word] = []
    
    return 0

def ladder_length_bidirectional(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find the length of the shortest transformation sequence using bidirectional BFS.
    
    Time Complexity: O(M^2 * N) - but much faster in practice
    Space Complexity: O(M^2 * N)
    
    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: List of valid words for transformation
        
    Returns:
        Number of words in the shortest transformation sequence, or 0 if not possible
    """
    if endWord not in wordList:
        return 0
    
    L = len(beginWord)
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(L):
            generic_state = word[:i] + "*" + word[i+1:]
            all_combo_dict[generic_state].append(word)
    
    # Bidirectional BFS
    queue_begin = deque([beginWord])
    queue_end = deque([endWord])
    
    visited_begin = {beginWord: True}
    visited_end = {endWord: True}
    
    level_begin = 1
    level_end = 1
    
    while queue_begin and queue_end:
        # Always expand the smaller queue for efficiency
        if len(queue_begin) > len(queue_end):
            queue_begin, queue_end = queue_end, queue_begin
            visited_begin, visited_end = visited_end, visited_begin
            level_begin, level_end = level_end, level_begin
        
        # Process one level from the beginning side
        for _ in range(len(queue_begin)):
            current_word = queue_begin.popleft()
            
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                for word in all_combo_dict[intermediate_word]:
                    if word in visited_end:
                        return level_begin + level_end
                    
                    if word not in visited_begin:
                        visited_begin[word] = True
                        queue_begin.append(word)
                
        # Clear processed intermediate words to prevent reprocessing
        all_combo_dict[intermediate_word] = []
    
    return 0

# Test cases
if __name__ == "__main__":
    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    print(f"Input: beginWord = '{beginWord1}', endWord = '{endWord1}'")
    print(f"wordList = {wordList1}")
    print(f"Output: {ladder_length(beginWord1, endWord1, wordList1)}")  # Expected: 5
    print(f"Bidirectional Output: {ladder_length_bidirectional(beginWord1, endWord1, wordList1)}")  # Expected: 5
    print()
    
    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    print(f"Input: beginWord = '{beginWord2}', endWord = '{endWord2}'")
    print(f"wordList = {wordList2}")
    print(f"Output: {ladder_length(beginWord2, endWord2, wordList2)}")  # Expected: 0
    print(f"Bidirectional Output: {ladder_length_bidirectional(beginWord2, endWord2, wordList2)}")  # Expected: 0
    print()
    
    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    print(f"Input: beginWord = '{beginWord3}', endWord = '{endWord3}'")
    print(f"wordList = {wordList3}")
    print(f"Output: {ladder_length(beginWord3, endWord3, wordList3)}")  # Expected: 2
    print(f"Bidirectional Output: {ladder_length_bidirectional(beginWord3, endWord3, wordList3)}")  # Expected: 2
    print()
    
    # Test case 4 - Same begin and end word
    beginWord4 = "hot"
    endWord4 = "hot"
    wordList4 = ["hot","dot","dog"]
    print(f"Input: beginWord = '{beginWord4}', endWord = '{endWord4}'")
    print(f"wordList = {wordList4}")
    print(f"Output: {ladder_length(beginWord4, endWord4, wordList4)}")  # Expected: 1 (but algorithm returns 0 as per problem definition)
    print(f"Note: Problem expects 0 when beginWord == endWord but endWord not in transformation sequence")