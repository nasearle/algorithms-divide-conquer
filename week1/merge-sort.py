def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        mergeSort(arr1)
        mergeSort(arr2)
        i = 0
        j = 0
        k = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1
        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1
        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1
        print arr

unsorted = [3, 2, 4, 1]

actual = mergeSort(unsorted)
expected = [1, 2, 3, 4]

print actual == expected
