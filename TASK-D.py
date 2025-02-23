import random
import csv

# Fitness function: Negative absolute difference between left and right pans
def calculate_fitness(solution, weights):
    left_sum = sum(w for w, s in zip(weights, solution) if s == 0)
    right_sum = sum(w for w, s in zip(weights, solution) if s == 1)
    return -abs(left_sum - right_sum)

# Generate a random initial solution (0 = left pan, 1 = right pan)
def random_solution(size):
    return [random.randint(0, 1) for _ in range(size)]

# Small change: Flip a random bit in the solution
def get_neighbor(solution):
    neighbor = solution.copy()
    index = random.randint(0, len(solution) - 1)
    neighbor[index] = 1 - neighbor[index]  # Flip 0 to 1 or 1 to 0
    return neighbor

# Hill Climbing for one restart
def hill_climbing(weights, max_iterations):
    current_solution = random_solution(len(weights))
    current_fitness = calculate_fitness(current_solution, weights)
    
    for _ in range(max_iterations):
        neighbor = get_neighbor(current_solution)
        neighbor_fitness = calculate_fitness(neighbor, weights)
        if neighbor_fitness > current_fitness:  # Maximize fitness (minimize difference)
            current_solution = neighbor
            current_fitness = neighbor_fitness
    
    return current_solution, current_fitness

# Random Restart Hill Climbing
def random_restart_hill_climbing(weights, num_restarts, max_iterations):
    best_solution = None
    best_fitness = float('-inf')
    results = []
    
    for restart in range(num_restarts):
        solution, fitness = hill_climbing(weights, max_iterations)
        results.append((restart, solution, fitness))
        if fitness > best_fitness:
            best_solution = solution
            best_fitness = fitness
    
    return best_solution, best_fitness, results

# Write dataset to CSV
def write_dataset_to_csv(weights, filename="dataset.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Weight"])
        for w in weights:
            writer.writerow([w])

# Read dataset from CSV without defaults
def read_dataset_from_csv(filename="dataset.csv"):
    weights = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row ("Weight")
        for row in reader:
            if row:  # Check if row is not empty
                weights.append(float(row[0]))
    if not weights:
        raise ValueError("No weights found in the CSV file.")
    return weights

# Write results to CSV
def write_results_to_csv(results, filename="results_TASK-D.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Restart", "Solution", "Fitness"])
        for restart, solution, fitness in results:
            writer.writerow([restart, solution, fitness])

# Main execution
if __name__ == "__main__":
    # Read weights from dataset.csv
    weights = read_dataset_from_csv()
    
    # Run Random Restart Hill Climbing
    num_restarts = 10
    max_iterations = 100
    best_solution, best_fitness, results = random_restart_hill_climbing(
        weights, num_restarts, max_iterations
    )
    
    # Write results to CSV
    write_results_to_csv(results)
    
    # Print results
    print(f"Weights: {weights}")
    print(f"Best Solution: {best_solution}")
    print(f"Best Fitness: {best_fitness}")
    left_sum = sum(w for w, s in zip(weights, best_solution) if s == 0)
    right_sum = sum(w for w, s in zip(weights, best_solution) if s == 1)
    print(f"Left Pan: {left_sum}, Right Pan: {right_sum}")