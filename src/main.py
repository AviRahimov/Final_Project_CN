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

# Loop through the CSV files
for df_name in (filter_list + youtube_list):
    df = pd.read_csv(df_name)

    # Create the bar histogram plot
    plt.figure(figsize=(10, 6))  # Set the figure size (optional)

    # Plot the bar histogram with size as bar width and time as bar height
    plt.bar(df['Time'], df['Length'], color='black', width=0.3)

    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Size')
    plt.title('Bar Histogram: Time vs. Size')

    # Create a directory named 'res' if it doesn't exist
    if not os.path.exists('res'):
        os.makedirs('res')
    # Save the plot as an image in the 'res' directory
    plt.savefig(f'res/{df_name[10:-4]}.png')

    # Show the plot (optional)
    plt.show()
