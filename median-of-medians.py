
import random
import time

def select_kth(arr, k):
    n = len(arr)

    if n <= 5:
        return sorted(arr)[k]
    
    medians = []
    for i in range(0, n, 5):
        group = arr[i:i+5]
        medians.append(sorted(group)[len(group)//2])
    
    pivot = select_kth(medians, len(medians)//2)

    lows = []
    highs = []
    pivots = []
    for x in arr:
        if x<pivot:
            lows.append(x)
        elif x>pivot:
            highs.append(x)
        else:
            pivots.append(x)
    
    if k < len(lows):
        return select_kth(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return select_kth(highs, k - len(lows)- len(pivots))
    

def sort_select_kth(arr, k):
    arr.sort()
    return arr[k]


def partition(arr, low, high, pivot_value):
    """Partition arr[low..high] around pivot_value. Returns final pivot index."""
    # find pivot index
    for i in range(low, high + 1):
        if arr[i] == pivot_value:
            arr[i], arr[high] = arr[high], arr[i]
            break

    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

def median_of_medians(arr, low, high):
    """Returns approximate median for pivoting"""
    n = high - low + 1
    if n <= 5:
        # sort small range in place
        arr[low:high+1] = sorted(arr[low:high+1])
        return arr[low + n // 2]

    # divide into groups of 5
    medians = []
    i = low
    while i <= high:
        sub_high = min(i + 4, high)
        arr[i:sub_high+1] = sorted(arr[i:sub_high+1])
        median_idx = i + (sub_high - i)//2
        medians.append(arr[median_idx])
        i += 5

    # recursively find median of medians
    return bfprt_select(medians, 0, len(medians)-1, len(medians)//2)

def bfprt_select(arr, low, high, k):
    """Select k-th smallest in arr[low..high] in place"""
    while True:
        if low == high:
            return arr[low]

        pivot_value = median_of_medians(arr, low, high)
        pivot_index = partition(arr, low, high, pivot_value)
        rank = pivot_index - low  # rank of pivot in current range

        if k == rank:
            return arr[pivot_index]
        elif k < rank:
            high = pivot_index - 1
        else:
            k = k - rank - 1
            low = pivot_index + 1
def bfprt_select_kth(arr, k):
    return bfprt_select(arr, 0, len(arr)-1, k)

def benchmark_kth(arr, k, funcs):
    """
    Benchmark multiple k-th selection functions on the same array.
    funcs: list of (name:str, function: callable(arr,k) -> kth_element)
    """
    results = {}
    n = len(arr)
    print(f"Array length: {n}, k = {k}")
    print("-" * 40)

    for func in funcs:
        test_arr = arr[:]  # copy for fair comparison
        t0 = time.perf_counter()
        ans = func(test_arr, k)
        t1 = time.perf_counter()
        results[func.__name__] = ans
        print(f"{func.__name__:20} | result = {ans:10} | time = {t1 - t0:.6f} s")

    # Check all results match
    unique_results = set(results.values())
    if len(unique_results) == 1:
        print("All results match ✅")
    else:
        print("Results differ ❌", results)

    print("-" * 40)


if __name__ == "__main__":
    random.seed(1337)
    n = random.randrange(999_999, 9_999_999)
    arr = [random.randrange(-10000, 10000)for _ in range(n)]
    k = n // 2

    benchmark_kth(arr, k, [select_kth, sort_select_kth, bfprt_select_kth])

    

    




    