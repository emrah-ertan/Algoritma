def sort(arr):
    if (type(arr) != list):
        print("Bubble_Sort.sort fonksiyon parametresi list tipinde olmalıdır.")
        return
    else:
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr