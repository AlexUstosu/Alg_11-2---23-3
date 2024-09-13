import random as rnd
import time

def bubleSort(array, n):
    for i in range(n):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Обмен элементов
    return array

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

massiv = [rnd.randint(0,20) for i in range(10000)]

print('Buble sort')
time_start_1 = time.perf_counter()
print(bubleSort(massiv, len(massiv)))
time_end_1 = time.perf_counter()
print(f'START: {time_start_1}   END: {time_end_1}   DURATION: {time_end_1 - time_start_1}')

print('Merge sort')
time_start_2 = time.perf_counter()
print(mergeSort(massiv))
time_end_2 = time.perf_counter()
print(f'START: {time_start_2}   END: {time_end_2}   DURATION: {time_end_2 - time_start_2}')


