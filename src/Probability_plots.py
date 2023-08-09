import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os

matplotlib.use("TkAgg")

# Load the CSV file into a DataFrame
filter_list = ['resources\\WITH_TCP_FILTER_TARGET1.csv', 'resources\\WITH_TCP_FILTER_TARGET2.csv',
               'resources\\WITH_TCP_FILTER_TARGET3.csv', 'resources\\WITH_TCP_FILTER_TARGET4.csv']
youtube_list = ['resources\\YOUTUBE_BACKGROUND_TARGET1.csv', 'resources\\YOUTUBE_BACKGROUND_TARGET2.csv',
                'resources\\YOUTUBE_BACKGROUND_TARGET3.csv', 'resources\\YOUTUBE_BACKGROUND_TARGET4.csv']
concat_list = filter_list + youtube_list

times_list = []
for i in range(len(concat_list)):
    df = pd.read_csv(concat_list[i])
    time_list = df['Time'].values.tolist()
    times_list.append(list(map(round, time_list)))

# Given inter-arrival times
inter_arrival_times = []
for i in range(len(times_list)):
    inter_arrival_times.append([times_list[i] - times_list[i - 1])

# Calculate kernel density estimation
kde = gaussian_kde(inter_arrival_times)

# Define the range of x values
x_values = np.linspace(min(inter_arrival_times), max(inter_arrival_times), 1000)

# Calculate the corresponding y values (probability density)
y_values = kde(x_values)

# Create the plot
plt.plot(x_values, y_values)
plt.xlabel('Inter-Arrival Time')
plt.ylabel('Probability Density')
plt.title('Probability Density of Inter-Arrival Times')
plt.show()
