# This main will be use as workspace for quick tests and for review.

from data_structures.Heaps.Heaps import MaxHeap


def form_max_heap(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            continue
        else:
            return i - 1
    return len(arr) - 1


def main():
    heap = MaxHeap()
    heap.insert(4)
    heap.insert(5)
    heap.insert(2)

    print(heap.second_max())

    print("Works")


main()
