import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

# Load the CSV file into a DataFrame
filter_list = ['resources\\WITH_TCP_FILTER_TARGET1.csv', 'resources\\WITH_TCP_FILTER_TARGET2.csv',
               'resources\\WITH_TCP_FILTER_TARGET3.csv', 'resources\\WITH_TCP_FILTER_TARGET4.csv']
youtube_list = ['resources\\YOUTUBE_BACKGROUND_TARGET1.csv', 'resources\\YOUTUBE_BACKGROUND_TARGET2.csv',
                'resources\\YOUTUBE_BACKGROUND_TARGET3.csv', 'resources\\YOUTUBE_BACKGROUND_TARGET4.csv']
concat_list = filter_list + youtube_list

# list of lists that contain for each csv file the times column as a list format
times_list = []
for i in range(len(concat_list)):
    df = pd.read_csv(concat_list[i])
    time_list = df['Time'].values.tolist()
    times_list.append(list(map(round, time_list)))

# Given inter-arrival times for each csv file
inter_arrival_times = [[], [], [], [], [], [], [], []]
for i in range(len(times_list)):
    for j in range(1, len(times_list[i])):
        inter_arrival_times[i].append(times_list[i][j] - times_list[i][j - 1])

index = 0
for delay in inter_arrival_times:
    recording_name = concat_list[index][10:-4]
    max_value = max(delay)
    bins = np.arange(0, max_value + 1)

    # Create the bar histogram plot
    plt.figure(figsize=(10, 6))  # Set the figure size (optional)
    # Plot the histogram
    plt.hist(delay, bins=bins, density=True, alpha=0.5, label='Histogram', color="cyan")

    # Fit an exponential distribution to the data
    mu = np.mean(delay)
    fit_x = np.linspace(0, max_value, 100)
    fit_y = (1 / mu) * np.exp(-fit_x / mu)
    normalize_param = max(fit_y)
    fit_y = fit_y / normalize_param
    plt.plot(fit_x, fit_y, 'r-', label='Exponential Fit')

    plt.xlabel('Inter-Arrival Time (seconds)')
    plt.ylabel('Probability Density')
    plt.title(f'Histogram of Inter-Arrival Times for recording: "{recording_name}"')
    plt.savefig(f'res/{recording_name}_PDF_PLOT.png')
    plt.show()
    index += 1
