# Step 1: Create the list of temperatures
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# Step 2: Print the first and last readings
print("First reading (index 0):", temperatures[0])
print("Last reading (index -1):", temperatures[-1])

# Step 3: Extract the "Afternoon Peak" readings (4th, 5th, 6th items)
afternoon_peak = temperatures[3:6]  # index 3 to 5
print("Afternoon Peak readings:", afternoon_peak)

# Step 4: Extract the "Last 3 Hours" readings using negative slicing
last_3_hours = temperatures[-3:]  # last 3 items
print("Last 3 Hours readings:", last_3_hours)
