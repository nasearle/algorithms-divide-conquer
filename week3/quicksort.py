class CountComparisons():
    def __init__(self):
        self.comparisons = 0
        self.array = []
    def quickSortandCount(self, start, end):
        if not start < end:
            return
        self.comparisons += end - start
        i = start + 1
        j = start + 1
        pivot = self.array[start]
        # pivot = self.array[end]
        # self.array[start], self.array[end] = self.array[end], self.array[start]
        # subarray = self.array[start:end + 1]
        # subarray_len = end - start
        # mid = subarray[subarray_len/2]
        # first = self.array[start]
        # last = self.array[end]
        # if first <= mid <= last or last <= mid <= first:
        #     pivot = mid
        #     self.array[start], self.array[start+subarray_len/2] = self.array[start+subarray_len/2], self.array[start]
        # elif mid <= first <= last or last <= first <= mid:
        #     pivot = first
        # else:
        #     pivot = last
        #     self.array[start], self.array[end] = self.array[end], self.array[start]
        while j <= end:
            if self.array[j] < pivot:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1
            j += 1
        self.array[i-1], self.array[start] = self.array[start], self.array[i-1]
        self.quickSortandCount(start, i-2)
        self.quickSortandCount(i, end)


file = open('quicksort.txt', "r")
lines = file.read().split('\r\n')
unsorted = map(int, lines)

# unsorted = [3, 2, 5, 7, 6, 1, 8, 4]
# unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
# unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
# unsorted = [5, 2, 7]

count = CountComparisons()
count.array = unsorted

actual = count.quickSortandCount(0, len(unsorted) - 1)

print count.array
print count.comparisons
