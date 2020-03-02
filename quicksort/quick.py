# high level description

# Quicksort(array A, lenght n)
# if n = 1 return
# p = choosePivot(A, n)
# Partition A around p
# recursively sort 1st part
# recursively sort 2nd part

def quicksort(array):

    smaller = []
    equal = []
    bigger = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                smaller.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                bigger.append(x)
        return quicksort(smaller)+equal+quicksort(bigger)
    else:
        return array


print(quicksort([8,7,6,5,4,3,2,1, 5,43, 2, 11, 19, 98, 2, 3, 6, 16, 32]))