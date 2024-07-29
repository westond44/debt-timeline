import matplotlib.pyplot as plt
from datetime import datetime

# Data preparation
events = [
    "Pre-1930s: Limited consumer credit;\nprimary focus of debt included\nmortgages and business loans.",
    "Post-WWII (1940s-1950s): Expansion\nof consumer credit",
    "1950: Introduction of\nDiners Club card",
    "1960s-1970s: Growth in consumer debt\nwith bank-issued credit cards.",
    "1965: Federal Government starts\nguaranteeing student loans.",
    "1980s: Deregulation of\nfinancial markets",
    "1990s: Boom in the\ncredit market",
    "2000-2007: Massive increase in\nconsumer debt",
    "2008 Financial Crisis:\nMajor recession",
    "2009: CARD Act of 2009",
    "Post-Recession Recovery:\nHigh levels of student loan debt",
    "Late 2010s: Record levels\nof consumer debt",
    "Pandemic impact:\nSharp increase in unsecured debt",
    "Post-Pandemic Era:\nUnsecured debt levels continue to rise"
]

dates = [
    "1929-01-01",
    "1945-01-01",
    "1950-01-01",
    "1960-01-01",
    "1965-01-01",
    "1980-01-01",
    "1990-01-01",
    "2000-01-01",
    "2008-01-01",
    "2009-01-01",
    "2010-01-01",
    "2017-01-01",
    "2020-01-01",
    "2022-01-01"
]

# Convert date strings to datetime objects
dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Define colors for different periods
colors = [
    "red",   # Pre-1930s
    "orange",   # 1940s-1950s
    "yellow",   # 1960s-1970s
    "green",   # 1980s
    "blue",   # 1990s
    "purple",  # 2000s
    "brown",  # 2010s
    "pink"  # 2020s
]

# Map events to colors based on the period they belong to
event_colors = [
    colors[0], colors[1], colors[1], colors[2], colors[2],
    colors[3], colors[4], colors[4], colors[5], colors[5],
    colors[6], colors[6], colors[7], colors[7]
]

# Plotting the timeline
plt.figure(figsize=(15, 8))

# Remove y-axis by setting all y values to the same point (e.g., y=0)
y_position = 0

# Adjust vertical spacing increment
spacing_increment = 1.5

# Create two lists for vertical positions to avoid overlap
upper_y_positions = []
lower_y_positions = []

for i in range(len(events)):
    if i % 2 == 0:
        upper_y_positions.append(spacing_increment * (len(upper_y_positions) + 1))
    else:
        lower_y_positions.append(-spacing_increment * (len(lower_y_positions) + 1))

# Plot each event
for i, (event, date, color) in enumerate(zip(events, dates, event_colors)):
    plt.plot(date, y_position, "o", markersize=10, color=color)
    # Assign upper or lower y position
    if i % 2 == 0:
        y_pos = upper_y_positions.pop(0)
        plt.text(date, y_pos, event, va='bottom', ha='center', fontsize=10, rotation=10, color='black')
        plt.plot([date, date], [y_position, y_pos], color='gray', linestyle='--')
    else:
        y_pos = lower_y_positions.pop(0)
        plt.text(date, y_pos, event, va='top', ha='center', fontsize=10, rotation=10, color='black')
        plt.plot([date, date], [y_position, y_pos], color='gray', linestyle='--')

# Remove y-ticks and y-labels
plt.yticks([])
plt.ylim(-15, 15)  # Further adjust vertical limits to make room for text
plt.xlabel('Date')
plt.title('Timeline of Unsecured Debt')
plt.grid(True, axis='x')  # Only show grid lines on x-axis

# Format x-axis to show years only
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))

# Add a legend
periods = ["Pre-1930s", "1940s-1950s", "1960s-1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
plt.legend(handles, periods, loc='upper left', title="Periods")

plt.tight_layout()

# Show the plot
plt.show()