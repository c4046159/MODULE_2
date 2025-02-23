import time
import random
import heapq
import csv

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def generate_random_dataset(size):
    return [random.randint(1, 100000) for _ in range(size)]

def measure_time(sort_function, data):
    start_time = time.perf_counter()
    sorted_data = sort_function(data[:])
    return (time.perf_counter() - start_time) * 1000

def run_experiments(sizes, runs=5):
    results = []
    for size in sizes:
        bubble_times = []
        heap_times = []
        for _ in range(runs):
            dataset = generate_random_dataset(size)
            bubble_times.append(measure_time(bubble_sort, dataset))
            dataset = generate_random_dataset(size)  # Regenerate to avoid reuse
            heap_times.append(measure_time(heap_sort, dataset))
        results.append((size, sum(bubble_times)/runs, sum(heap_times)/runs))
    return results

def save_results_to_csv(results, filename="results.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Dataset Size", "Bubble Sort Time (ms)", "Heap Sort Time (ms)"])
            writer.writerows(results)
    except IOError as e:
        print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    dataset_sizes = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    experiment_results = run_experiments(dataset_sizes)
    save_results_to_csv(experiment_results)
    print("The experiment is now completed.\nResults saved to results.csv.")