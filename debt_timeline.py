import matplotlib.pyplot as plt
from datetime import datetime

# Data preparation
events = [
    "Limited consumer credit",
    "Consumer credit expands",
    "Diners Club card intro",
    "Growth in credit cards",
    "Govt guarantees student loans",
    "Financial deregulation",
    "Credit market boom",
    "Consumer debt surge",
    "Major recession",
    "CARD Act 2009",
    "High student loan debt",
    "Record consumer debt",
    "Rise in unsecured debt",
    "Unsecured debt increase"
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

# Set all y values to the same point (y=0)
y_position = 0

# Adjust vertical spacing increment for clearer event distribution
spacing_increment = 2.5

# Use a pattern to assign positions above and below the timeline consistently
y_positions = [-spacing_increment, spacing_increment] * (len(events) // 2 + 1)

# Plot each event
for i, (event, date, color) in enumerate(zip(events, dates, event_colors)):
    plt.plot(date, y_position, "o", markersize=10, color=color)
    plt.text(date, y_positions[i], event, va='bottom' if y_positions[i] > 0 else 'top', 
             ha='center', fontsize=10, rotation=45, color='black')

# Remove y-ticks and y-labels
plt.yticks([])
plt.ylim(-spacing_increment * 3, spacing_increment * 3)  # Adjust vertical limits
plt.xlabel('Date')
plt.title('Timeline of Unsecured Debt')
plt.grid(True, axis='x')  # Only show grid lines on x-axis

# Format x-axis to show years only
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))

# Add a legend
periods = ["Pre-1930s", "1940s-1950s", "1960s-1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
plt.legend(handles, periods, loc='upper left', title="Periods")

# Remove plot borders
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()

# Show the plot
plt.show()