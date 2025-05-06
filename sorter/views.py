from django.shortcuts import render

def sorting_view(request):
    sorted_list = []
    algorithm = ''
    if request.method == 'POST':
        data = request.POST.get('numbers')
        algorithm = request.POST.get('algorithm')
        if data:
            try:
                numbers = list(map(int, data.split(',')))
                if algorithm == 'insertion':
                    sorted_list = insertion_sort(numbers)
                elif algorithm == 'selection':
                    sorted_list = selection_sort(numbers)
                elif algorithm == 'bubble':
                    sorted_list = bubble_sort(numbers)
                elif algorithm == 'quick':
                    sorted_list = quick_sort(numbers)
                elif algorithm == 'merge':
                    sorted_list = merge_sort(numbers)
                elif algorithm == 'heap':
                    sorted_list = heap_sort(numbers)
            except ValueError:
                sorted_list = ['Invalid input! Use comma-separated numbers.']

    return render(request, 'sorting.html', {
        'sorted_list': sorted_list,
        'selected_algorithm': algorithm
    })

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(arr):
    import heapq
    h = arr[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
