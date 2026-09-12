# Python Backend Interview Solutions - 3 Day Plan

This repository contains solutions to all LeetCode problems from the 3-day Python backend interview preparation plan.

## Repository Structure
```
python-backend-interview-3day-solutions/
├── README.md
└── solutions/
    ├── 0001_two_sum.py
    ├── 0002_reverse_integer.py
    ├── 0003_palindrome_number.py
    ├── 0004_merge_intervals.py
    ├── 0005_insert_interval.py
    ├── 0006_lru_cache.py
    ├── 0007_reverse_linked_list.py
    ├── 0008_merge_two_sorted_lists.py
    ├── 0009_copy_list_with_random_pointer.py
    ├── 0010_course_schedule.py
    ├── 0011_number_of_islands.py
    ├── 0012_kth_largest_element.py
    ├── 0013_top_k_frequent_elements.py
    ├── 0014_word_ladder.py
    └── 0015_alien_dictionary.py
```

## Day-wise Problem Breakdown

### Day 1: Python Fundamentals & Basic Data Structures
- **0001_two_sum.py** - Two Sum (#1)
- **0002_reverse_integer.py** - Reverse Integer (#7)
- **0003_palindrome_number.py** - Palindrome Number (#9)
- **0004_merge_intervals.py** - Merge Intervals (#56)
- **0005_insert_interval.py** - Insert Interval (#57)
- **0006_lru_cache.py** - LRU Cache (#146)

### Day 2: Linked Lists, Trees & Graphs
- **0007_reverse_linked_list.py** - Reverse Linked List (#206)
- **0008_merge_two_sorted_lists.py** - Merge Two Sorted Lists (#21)
- **0009_copy_list_with_random_pointer.py** - Copy List with Random Pointer (#138)
- **0010_course_schedule.py** - Course Schedule (#207)
- **0011_number_of_islands.py** - Number of Islands (#200)

### Day 3: Advanced Algorithms & System Design Concepts
- **0012_kth_largest_element.py** - Kth Largest Element in an Array (#215)
- **0013_top_k_frequent_elements.py** - Top K Frequent Elements (#347)
- **0014_word_ladder.py** - Word Ladder (#127)
- **0015_alien_dictionary.py** - Alien Dictionary (#269)

## Key Concepts Covered

### Data Structures
- Arrays/Lists
- Hash Maps/Dictionaries
- Linked Lists (singly, with random pointers)
- Trees (implicit in course schedule)
- Graphs (explicit in word ladder, alien dictionary)
- Heaps/Priority Queues
- Queues (for BFS)
- Stacks (for DFS)

### Algorithms
- Two Pointers Technique
- Binary Search
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Topological Sort
- Greedy Algorithms
- Dynamic Programming (LRU Cache)
- QuickSelect
- Bucket Sort

### System Design Concepts (from study plan)
- REST API Design Principles
- Docker Containerization
- SQLAlchemy ORM
- AsyncIO and Concurrency
- System Design (URL Shortener, Rate Limiting, Caching)
- Behavioral Interview Preparation (STAR method)

## Running the Solutions

Each solution file can be run independently:
```bash
python solutions/0001_two_sum.py
```

All solutions include:
- Clean, readable implementation
- Time and space complexity analysis
- Multiple approaches where applicable
- Comprehensive test cases
- Detailed comments explaining the logic

## Interview Preparation Topics (Beyond LeetCode)

Based on the 3-day plan, also review:
1. **Python Fundamentals**: OOP, decorators, generators, context managers
2. **System Design**: REST API design, HTTP methods, status codes, versioning
3. **DevOps**: Docker fundamentals, docker-compose, containerizing Python apps
4. **Database**: SQLAlchemy core vs ORM, session management, relationships
5. **Concurrency**: AsyncIO, threading vs multiprocessing vs asyncio, GIL explanation
6. **API Development**: REST API design with FastAPI
7. **Advanced DB**: Indexing, transactions, ACID, ORM querying
8. **System Design Exercises**: URL shortener design, rate limiting, caching
9. **Behavioral**: STAR method preparation
10. **Mock Interview Practice**

## Complexity Analysis Summary

| Problem | Approach | Time Complexity | Space Complexity |
|---------|----------|-----------------|------------------|
| Two Sum | Hash Map | O(n) | O(n) |
| Reverse Integer | Mathematical | O(log x) | O(1) |
| Palindrome Number | Mathematical | O(log x) | O(1) |
| Merge Intervals | Sorting + Merge | O(n log n) | O(n) |
| Insert Interval | Line Sweep | O(n) | O(n) |
| LRU Cache | Hash Map + DLL | O(1) | O(capacity) |
| Reverse Linked List | Iterative | O(n) | O(1) |
| Merge Two Sorted Lists | Two Pointers | O(n+m) | O(1) |
| Copy List w/ Random Pointer | Hash Map | O(n) | O(n) |
| Course Schedule | Topological Sort (BFS) | O(V+E) | O(V+E) |
| Number of Islands | BFS/DFS | O(m×n) | O(min(m,n)) |
| Kth Largest Element | Min-Heap | O(n log k) | O(k) |
| Top K Frequent | Heap/Bucket Sort | O(n + k log n) / O(n) | O(n) |
| Word Ladder | BFS | O(M²×N) | O(M²×N) |
| Alien Dictionary | Topological Sort | O(C) | O(U+min(U,E)) |

Where:
- n = array/list length
- m, n = grid dimensions
- k = target rank/frequency
- V, E = vertices/edges in graph
- M = word length
- N = number of words
- U = unique letters
- C = total characters in all words

Good luck with your Python backend interview preparation! 🚀