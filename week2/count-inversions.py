class CountInversion():
    def __init__(self):
        self.count = 0
    def mergeSortandCount(self, arr):
        if len(arr) > 1:
            mid = len(arr)/2
            arr1 = arr[:mid]
            arr2 = arr[mid:]
            self.mergeSortandCount(arr1)
            self.mergeSortandCount(arr2)
            # print self.count
            i = 0
            j = 0
            k = 0
            output = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                    self.count += len(arr1[i:])
                k += 1
            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1
            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1
            return self.count

file = open('integers.txt', "r")
lines = file.read().split('\r\n')
unsorted = map(int, lines)

count = CountInversion()

actual = count.mergeSortandCount(unsorted)

print actual
