def sort(arr):
    if (type(arr) != list):
        print("Counting_Sort.sort fonksiyon parametresi list tipinde olmalıdır.")
        return
    else:
        max_val = max(arr)  # Dizideki maksimum değeri bul
        min_val = min(arr)  # Dizideki minimum değeri bul
        count = [0] * (max_val - min_val + 1)  # Sayacı oluştur

        for num in arr:
            count[num - min_val] += 1

        sorted_arr = []
        for i, count in enumerate(count):
            sorted_arr.extend([i + min_val] * count)
    return sorted_arr