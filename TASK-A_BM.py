
# 1. Generate random stall positions: random.randint()
import random

def generate_stalls(n, min_val=1, max_val=100):
    print("Generates 'n' random stall positions and sorts them.")
    stalls = sorted(random.sample(range(min_val, max_val), n))
    return stalls

# Step 2: For each distance, begin by placing cows at the first stall and check if 
# If (current position  –  previous position >= distance)
#    True: update previous position = current position, check next distance.
    
def distance_OK(stalls, d, cows):
    print ("Check if it is possible to place",cows,"with at least",d,"distance apart.")
    count = 1  # Place first cow in the first stall
    last_position = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= d:
            count += 1
            last_position = stalls[i]
            if count == cows:
                return True
    else:
        return False

def aggressiveCows(stalls, cows):
    print ("Finds the maximum minimum distance to place",cows, "cows","in",stalls)
    min_d, max_d = 1, stalls[-1] - stalls[0]
    best_d = 0
    
    for d in range(min_d, max_d + 1):
        if distance_OK(stalls, d, cows):
            best_d = d  # Update best found distance
        else:
            break  # Stop checking when a distance is no longer possible
    
    return best_d

stall_count = 5
cow_count = 3
stalls = generate_stalls(stall_count, 1, 20)  # Generate random stalls in range 1 to 20
print("Stall Positions:", stalls)
best_distance = aggressiveCows(stalls, cow_count)
print("Largest minimum distance:", best_distance)
