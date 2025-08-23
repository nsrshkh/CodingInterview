# from GeneralConcepts import timer
# import time
#
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
#
#
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
#
# # Example usage
# arr = [5, 2, 9, 1, 5, 6, 0, 6, 3, 7, 8, 4, 2, 1, 9, 5, 3, 7, 8, 4, 0, 6, 2, 1, 9, 5, 3, 7, 8, 4, 5, 2, 9, 1, 5, 6, 0, 6, 3, 7, 8, 4, 2, 1, 9, 5, 3, 7, 8, 4, 0, 6, 2, 1, 9, 5, 3, 7, 8, 4]
# start = time.time()
# print(start)
# sorted_arr = merge_sort(arr)
# # time.sleep(0.5)
# end = time.time()
# print(end)
# print(sorted_arr)
# print(f"merge_sort took {end-start:.5f} seconds")


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(quicksort(left) + middle + quicksort(right))
    return quicksort(left) + middle + quicksort(right)

# Example usage
arr = [5, 2, 9, 1, 5, 6, 0, 6, 3, 7, 8, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)
