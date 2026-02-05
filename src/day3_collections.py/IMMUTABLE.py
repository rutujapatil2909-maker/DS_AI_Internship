# Step 1: Create a tuple for screen resolution
screen_res = (1920, 1080)

# Step 2: Print the current resolution
print("Current Resolution:", f"{screen_res[0]}x{screen_res[1]}")

# Step 3: Experiment - Try to change the width (this will cause an error)
# screen_res[0] = 1280  # This line will cause a TypeError

# Step 4: Explain immutability
print("Tuples cannot be modified!")
