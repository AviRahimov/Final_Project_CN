import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

# Load the CSV file into a DataFrame
# Define lists of file paths
filter_list = ['resources\\WITH_TCP_FILTER_TARGET1.csv', 'resources\\WITH_TCP_FILTER_TARGET2.csv',
               'resources\\WITH_TCP_FILTER_TARGET3.csv', 'resources\\WITH_TCP_FILTER_TARGET4.csv']
youtube_list = ['resources\\YOUTUBE_BACKGROUND_TARGET1.csv', 'resources\\YOUTUBE_BACKGROUND_TARGET2.csv',
                'resources\\YOUTUBE_BACKGROUND_TARGET3.csv', 'resources\\YOUTUBE_BACKGROUND_TARGET4.csv']

# Combine the lists
concat_list = filter_list + youtube_list

# Prepare list of times for each dataset
times_list = []
for i in range(len(concat_list)):
    # Load data from CSV
    df = pd.read_csv(concat_list[i])
    time_list = df['Time'].values.tolist()

    # Round the time values and add to the list
    times_list.append(list(map(round, time_list)))

# Given inter-arrival times for each csv file
packet_delay_data = [[], [], [], [], [], [], [], []]
for i in range(len(times_list)):
    for j in range(1, len(times_list[i])):
        # Calculate inter-arrival times and add to the list
        packet_delay_data[i].append(times_list[i][j] - times_list[i][j - 1])

index = 0
# Create Q-Q plots for each dataset
for data in packet_delay_data:
    recording_name = concat_list[index][10:-4]

    # Create a new figure for each dataset
    plt.figure(figsize=(6, 4))

    sorted_data = np.sort(data)
    # Normalize the data to [0, 1] range
    normalized_data = (np.array(sorted_data) - np.min(sorted_data)) / (np.max(sorted_data) - np.min(sorted_data))

    # Scatter plot of data points
    plt.scatter(sorted_data, np.sort(normalized_data), marker='o', color='cyan', alpha=0.7,
                label='Inter-Arrival Times Data')

    # Add a pink line representing the expected distribution
    plt.plot(sorted_data, np.sort(normalized_data), color='magenta', linewidth=2, label='Expected Distribution')

    # Labels and title
    plt.xlabel('Delays Distribution Data')
    plt.ylabel('Normalized Sample Quantiles')
    plt.title(f'Q-Q Plot - Dataset {recording_name}')
    plt.legend()  # Add a legend to show the pink line label

    # Save the plot as an image
    plt.savefig(f'res/{recording_name}_Q-Q_PLOT.png')

    # Show the plot
    plt.show()

    index += 1
