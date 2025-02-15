
import random

def generate_initial_solution(n):
    """Generates a random initial solution (binary list)."""
    return [random.choice([0, 1]) for _ in range(n)]

def fitness(solution, weights):
    """Computes the absolute difference between two sides of the scale."""
    left_weight = sum(weights[i] for i in range(len(solution)) if solution[i] == 0)
    right_weight = sum(weights[i] for i in range(len(solution)) if solution[i] == 1)
    return abs(left_weight - right_weight)

def mutate(solution):
    """Performs a small change by flipping one bit."""
    new_solution = solution[:]
    index = random.randint(0, len(solution) - 1)
    new_solution[index] = 1 - new_solution[index]
    return new_solution

def hill_climb(weights, max_iterations=1000):
    """Performs standard hill climbing on the Scales Problem."""
    solution = generate_initial_solution(len(weights))
    best_fitness = fitness(solution, weights)
    
    for _ in range(max_iterations):
        new_solution = mutate(solution)
        new_fitness = fitness(new_solution, weights)
        if new_fitness < best_fitness:
            solution, best_fitness = new_solution, new_fitness
    
    return solution, best_fitness

def random_restart_hill_climbing(weights, num_restarts=10, max_iterations=1000):
    """Performs RRHC with multiple restarts."""
    best_solution = None
    best_fitness = float('inf')
    
    for _ in range(num_restarts):
        solution, fitness_value = hill_climb(weights, max_iterations)
        if fitness_value < best_fitness:
            best_solution, best_fitness = solution, fitness_value
    
    return best_solution, best_fitness

# Example usage
if __name__ == "__main__":
    weights = [1, 3, 4, 7, 9, 11, 14, 18]  # Example dataset
    best_solution, best_fitness = random_restart_hill_climbing(weights)
    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
