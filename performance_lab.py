# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    return max(counts, key=counts.get)


    # --- Tests ---
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5]) == 5                      # single element
assert most_frequent([7, 7, 7, 7]) == 7             # all identical
assert most_frequent([-1, -1, 2]) == -1             # negatives
assert most_frequent([1, 2, 3, 4]) in {1, 2, 3, 4}  # all unique (any is valid)
assert most_frequent([1, 1, 2, 2]) in {1, 2}        # tie (any is valid)
assert most_frequent([]) is None  
print("Problem 1: all tests passed")

"""
Time and Space Analysis for problem 1:
- Best-case: 0(n)
- Worst-case: 0(n)
- Average-case: 0(n)
- Space complexity: 0(k)
- Why this approach? a set would rescan all distict values which would be slower when scaled 
- Could it be optimized? If there is a set range amount if could be easier to optimize because an array is faster. 
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    dupfree = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            dupfree.append(n)
    return dupfree
    
# --- Tests ---
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([]) == []                        # empty list
assert remove_duplicates([1]) == [1]                      # single element
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]          # no duplicates
assert remove_duplicates([2, 2, 2, 2]) == [2]             # all identical
assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]    # order preserved
assert remove_duplicates([-1, 0, -1, 0]) == [-1, 0]       # negatives and zero
print("Problem 2: all tests passed")
"""
Time and Space Analysis for problem 2:
- Best-case:0(n)
- Worst-case: 0(n)
- Average-case: 0(n)
- Space complexity: 0(k)
- Why this approach? a set is for checking for dups on average and works better for a list. 
- Could it be optimized? You could maybe try to use lists. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.append((min(n, complement), max(n, complement)))
        seen.add(n)
    return pairs

# --- Tests ---

assert sorted(find_pairs([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]
assert find_pairs([], 5) == []                            
assert find_pairs([3], 6) == []                        
assert find_pairs([1, 2, 3], 10) == []                   
assert find_pairs([2, 3, 4], 4) == []                       
assert sorted(find_pairs([-2, 2, 0, 5], 0)) == [(-2, 2)]  
assert sorted(find_pairs([1, 2, 3, 4, 5, 6], 7)) == [(1, 6), (2, 5), (3, 4)]  
assert sorted(find_pairs([5, 1, 4, 2], 6)) == [(1, 5), (2, 4)]  
print("Problem 3: all tests passed")

"""
Time and Space Analysis for problem 3:
- Best-case: 0(n)
- Worst-case: 0(n)
- Average-case: 0(n)
- Space complexity: 0(n)
- Why this approach? it checks every pair with nester loops. 
- Could it be optimized? we could sort the list first which would make it easier to find pairs. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2                      
    storage = [None] * capacity       
    size = 0
    total_copies = 0

    for item in range(1, n + 1):
        if size == capacity:
            new_capacity = capacity * 2
            new_storage = [None] * new_capacity
            for i in range(size):   
                new_storage[i] = storage[i]
            total_copies += size
            print(f"Resize: capacity {capacity} -> {new_capacity}, copied {size} items")
            storage, capacity = new_storage, new_capacity
        storage[size] = item
        size += 1

    return storage[:size], total_copies


# --- Tests ---
items, copies = add_n_items(6)       
assert items == [1, 2, 3, 4, 5, 6]
assert copies == 2 + 4    
assert add_n_items(0) == ([], 0)     
assert add_n_items(1) == ([1], 0)   
assert add_n_items(2) == ([1, 2], 0)
assert add_n_items(3)[1] == 2        
assert add_n_items(9)[1] == 2 + 4 + 8

print("Problem 4: all tests passed")


"""
Time and Space Analysis for problem 4:
- When do resizes happen? when the list is full and a new item arrives
- What is the worst-case for a single append? an append that triggers a resize 
- What is the amortized time per append overall?
- Space complexity: 0(n)
- Why does doubling reduce the cost overall? the resizes pays for itself arrays exist togethers. 
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


# --- Tests ---
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([]) == []                      
assert running_total([5]) == [5]                     
assert running_total([0, 0, 0]) == [0, 0, 0]           
assert running_total([-1, -2, -3]) == [-1, -3, -6]    
assert running_total([3, -3, 4]) == [3, 0, 4]          
assert running_total([2, 2, 2, 2]) == [2, 4, 6, 8] 
print("Problem 5: all tests passed")
"""
Time and Space Analysis for problem 5:
- Best-case: 0(n)
- Worst-case: 0(n)
- Average-case: 0(n)
- Space complexity: 0(n)
- Why this approach? a aive computs sums for each index.
- Could it be optimized? if someone doesnt need to keep the orignial list the totals can be written in place.
"""
