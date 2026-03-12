import random

# 1. Generate Data
scores = [random.randint(40, 100) for i in range(10)]
print("Original Scores:", scores)

# 2. Quick Sort (recursive)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

sorted_scores = quick_sort(scores)
print("Sorted Scores:", sorted_scores)

# 3. Ask user for score
search_score = int(input("Enter the score you want to find: "))

# 4. Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

position = binary_search(sorted_scores, search_score)

if position != -1:
    print("Candidate with score", search_score, "found at rank", position)
else:
    print("Score not found in the list.")
