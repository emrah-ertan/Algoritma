def sort(arr):
    if (type(arr) != list):
        print("Insertion.Sort fonksiyon parametresi list tipinde olmalıdır.")
        return
    else:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr