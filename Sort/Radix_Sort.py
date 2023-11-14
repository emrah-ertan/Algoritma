def _counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def _radix_sort(arr):
    if(type(arr) != list):
        print("Radix_Sort.show_result fonksiyon parametresi list tipinde olmalıdır.")
        return
    else:
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            _counting_sort(arr, exp)
            exp *= 10
def show_result(arr):
    _radix_sort(arr)
    print("Radix Sort ile sıralanmış dizi:", arr)