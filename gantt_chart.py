import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Provided data
Data = {
    'Task': ['Task1', "Task2", "Task3"],
    'Start': ['6-2-24', '6-2-24', '20-2-24'],
    'End': ['11-2-24', '20-2-24', '1-3-24']
}

# Convert dates to datetime objects
Data['Start'] = pd.to_datetime(Data['Start'], format='%d-%m-%y')
Data['End'] = pd.to_datetime(Data['End'], format='%d-%m-%y')

# Create a DataFrame from the data
df = pd.DataFrame(Data)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the Gantt bars
for i, task in df.iterrows():
    ax.barh(task['Task'],
            left=task['Start'],
            width=(task['End'] - task['Start']),
            height=0.5,
            align='center',
            alpha=0.8,
            label='Duration')

# Set labels and title
ax.set_xlabel('Timeline')
ax.set_ylabel('Tasks')
ax.set_title('Gantt Chart')

# Set date format for x-axis
date_format = '%d-%m-%y'
ax.xaxis_date()
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter(date_format))

# Show grid and legend
ax.grid(True)
ax.legend()

# Autoformat date labels and display the plot
fig.autofmt_xdate()
plt.tight_layout()
plt.show()
