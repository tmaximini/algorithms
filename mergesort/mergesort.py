def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = round(len(arr) / 2)
    left = arr[:middle]
    right = arr[middle:]
    return merge(mergesort(left), mergesort(right))

def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left: 
            result.append(left.pop(0))
        elif right: 
            result.append(right.pop(0))     
    return result




# Complexity: O(n log(n))

print(mergesort([8,7,6,5,4,3,2,1, 5,43, 2, 11, 19, 98, 2, 3, 6, 16, 32]))