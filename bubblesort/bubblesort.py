def sort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        if not corrected:
            return arr



# best O(n)
print(sort([1,2,3,4,5,6,7,8]))
# average O(n^2)
print(sort([8,7,6,5,1,2,3,4]))
# worst O(n^2)
print(sort([8,7,6,5,4,3,2,1]))
