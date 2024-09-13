import random as rnd
import time
import sys

sys.setrecursionlimit(3000)
def simpleInversion(array):
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                count += 1
    return count


def splitInversion(array, n):
    count = 0
    if n == 0 or n == 1:
        return 0
    else:
        leftInvertions = splitInversion(array[:int(n/2)], int(n/2))
        rightInvertions = splitInversion(array[int(n/2):], int(n/2))
        splitInversions = splitInversion(array, n)
        count = leftInvertions + rightInvertions + splitInversions
    return count





def mergeSort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k]= left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k]= right[j]
            j += 1
            k += 1
        return numbers

massiv = [rnd.randint(0,20) for i in range(10)]

print('Simple Inversion')
time_start_1 = time.perf_counter()
print(simpleInversion(massiv))
time_end_1 = time.perf_counter()
print(f'START: {time_start_1}   END: {time_end_1}   DURATION: {time_end_1 - time_start_1}')

print('Split Inversion')
time_start_2 = time.perf_counter()
print(splitInversion(massiv, len(massiv)))
time_end_2 = time.perf_counter()
print(f'START: {time_start_2}   END: {time_end_2}   DURATION: {time_end_2 - time_start_2}')


