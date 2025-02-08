# Same as the Basic Method we start by generating a random number of stalls and sorting them. 

import random

def generate_stalls(n, min_val=1, max_val=100):
    stalls = sorted(random.sample(range(min_val, max_val), n))
    return stalls
    
def distance_OK(stalls, d, cows):
    # Checks if it's possible to place 'cows' with at least 'd' distance apart.
    count = 1  # Place first cow in the first stall
    last_position = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= d:
            count += 1
            last_position = stalls[i]
            if count == cows:
                return True
    
    return False

def aggressiveCows(stalls, cows):
    # Finds the maximum minimum distance to place cows in stalls using binary search.
    low, high = 1, stalls[-1] - stalls[0]
    best_d = 0
    
    while low <= high:
        mid = (low + high) // 2
        if distance_OK(stalls, mid, cows):
            best_d = mid  # Update best found distance
            low = mid + 1  # Try for a larger minimum distance
        else:
            high = mid - 1  # Reduce search space
    
    return best_d

# Example usage
stall_count = 5
cow_count = 3
stalls = generate_stalls(stall_count, 1, 20)  # Generate random stalls in range 1 to 20
print("Stall Positions:", stalls)
best_distance = aggressiveCows(stalls, cow_count)
print("Largest minimum distance:", best_distance)