import matplotlib.pyplot as plt
import csv

# Initialize empty dictionaries to store the data for each group
delays = {}
lengths = {}
colors = {"HTTP": "g", "TCP": "b", "UDP": "r"} # Assign different colors to different protocols

# Open and read the CSV file
with open("packets.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # Skip the header row
    prev_time = None # Initialize a variable to store the previous time value
    prev_protocol = None # Initialize a variable to store the previous protocol value
    for row in reader:
        time = float(row[1]) # Extract the time value from the second column
        protocol = row[4] # Extract the protocol value from the fifth column
        length = int(row[5]) # Extract the length value from the sixth column
        # Check if the protocol is already in the dictionaries, if not, create a new list for it
        if protocol not in delays:
            delays[protocol] = []
        if protocol not in lengths:
            lengths[protocol] = []
        # If the protocol is the same as the previous one, calculate the inter-message delay and append it to the list
        if protocol == prev_protocol:
            delay = time - prev_time
            delays[protocol].append(delay)
        # Append the length value to the list
        lengths[protocol].append(length)
        # Update the previous time and protocol values
        prev_time = time
        prev_protocol = protocol

# Plot the data for each group using a scatter plot
for protocol in delays:
    # Check if the lists have the same size
    if len(delays[protocol]) != len(lengths[protocol]):
        # If not, find the minimum size
        min_size = min(len(delays[protocol]), len(lengths[protocol]))
        # Truncate the longer list to match the shorter one
        delays[protocol] = delays[protocol][:min_size]
        lengths[protocol] = lengths[protocol][:min_size]

        plt.scatter(delays[protocol], lengths[protocol], color=colors[protocol], label=protocol)

# Label the axes and add a title and a legend to the plot
plt.xlabel("Inter-message delay (s)")
plt.ylabel("Message size (bytes)")
plt.title("Inter-message delays and message sizes by protocol")
plt.legend()
plt.show()
