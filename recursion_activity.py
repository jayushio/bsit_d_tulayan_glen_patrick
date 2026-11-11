
def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


def find_largest(arr):
    if len(arr) == 1:
        return arr[0]

    largest = find_largest(arr[1:])

    if arr[0] > largest:
        return arr[0]
    else:
        return largest


def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("SUM THE ARRAY")
print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4]))
print(sum_array([5, -2, 3, -1]))

print("\nFIND THE LARGEST NUMBER")
print(find_largest([5]))
print(find_largest([10, 5, 3, 2]))
print(find_largest([1, 4, 6, 9]))
print(find_largest([-5, -2, -8, -1]))

print("\nCOUNT A CHOSEN NUMBER")
print(count_number([], 5))
print(count_number([2, 1, 2, 3, 2, 4], 2))
print(count_number([1, 2, 3, 4], 5))
