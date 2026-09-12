"""
LeetCode Problem 269: Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted 
lexicographically by the rules of this new alien language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order 
by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Time Complexity: O(C) - Where C is total length of all words
Space Complexity: O(U + min(U, E)) - Where U is number of unique letters, E is number of edges
"""

from typing import List
from collections import defaultdict, deque

def alien_order(words: List[str]) -> str:
    """
    Determine the order of letters in alien dictionary using topological sort.
    
    Args:
        words: List of words sorted lexicographically in alien language
        
    Returns:
        String representing valid letter order, or empty string if impossible
    """
    # Step 1: Create adjacency list and in-degree count
    adj_list = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}
    
    # Step 2: Find all edges by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        
        # Find first differing character
        min_length = min(len(word1), len(word2))
        if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
            # Invalid case: "abc", "ab" - prefix longer than shorter word
            return ""
        
        for j in range(min_length):
            if word1[j] != word2[j]:
                # Found edge: word1[j] -> word2[j]
                if word2[j] not in adj_list[word1[j]]:
                    adj_list[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
    
    # Step 3: Topological sort using Kahn's algorithm
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for neighbor in adj_list[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all letters were processed (no cycle)
    if len(result) == len(in_degree):
        return "".join(result)
    else:
        return ""  # Cycle detected

# Test cases
if __name__ == "__main__":
    # Test case 1
    words1 = ["wrt","wrf","er","ett","rftt"]
    print(f"Input: words = {words1}")
    print(f"Output: '{alien_order(words1)}'")  # Expected: "wertf"
    print()
    
    # Test case 2
    words2 = ["z","x"]
    print(f"Input: words = {words2}")
    print(f"Output: '{alien_order(words2)}'")  # Expected: "zx"
    print()
    
    # Test case 3 - Invalid ordering
    words3 = ["z","x","z"]
    print(f"Input: words = {words3}")
    print(f"Output: '{alien_order(words3)}'")  # Expected: "" (cycle)
    print()
    
    # Test case 4 - Prefix case
    words4 = ["abc","ab"]
    print(f"Input: words = {words4}")
    print(f"Output: '{alien_order(words4)}'")  # Expected: "" (invalid prefix)
    print()
    
    # Test case 5 - Single word
    words5 = ["z"]
    print(f"Input: words = {words5}")
    print(f"Output: '{alien_order(words5)}'")  # Expected: "z"
    print()
    
    # Test case 6 - No relations
    words6 = ["ab","adc"]
    print(f"Input: words = {words6}")
    print(f"Output: '{alien_order(words6)}'")  # Expected: "abcd" or "adbc" etc.
    print()