def sort(arr):
    if (type(arr) != list):
        print("Quick_Sort.sort fonksiyon parametresi list tipinde olmalıdır.")
        return
    else:
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x <= pivot]
            right = [x for x in arr[1:] if x > pivot]
            return sort(left) + [pivot] + sort(right)