def _heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def heap_sort(arr):
    if (type(arr) != list):
        print("Quick_Sort.sort fonksiyon parametresi list tipinde olmalıdır.")
        return
    else:
        n = len(arr)

        # Max heap oluştur
        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)

        # Heap'ten sırala
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Root ile son elemanı değiştir
            _heapify(arr, i, 0)  # Yeniden düzenle

        return arr