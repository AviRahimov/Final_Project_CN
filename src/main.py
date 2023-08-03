import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use("TkAgg")

# Load the CSV file into a DataFrame
csv_file = 'src\YOUTUBE_BACKGROUND_TARGET2.csv'
df = pd.read_csv(csv_file)


# Create the bar histogram plot
plt.figure(figsize=(10, 6))  # Set the figure size (optional)

# Plot the bar histogram with size as bar width and time as bar height
plt.bar(df['Time'], df['Length'], color='black', width=0.3)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Size')
plt.title('Bar Histogram: Time vs. Size')

# Show the plot
plt.show()
