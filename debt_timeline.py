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

# Plotting the timeline
plt.figure(figsize=(15, 4))

# Remove y-axis by setting all y values to the same point (e.g., y=0)
y_position = 0

for i, (event, date) in enumerate(zip(events, dates)):
    plt.plot(date, y_position, "o", markersize=10)
    # Alternate the position of the text above and below the line to prevent overlap
    if i % 2 == 0:
        plt.text(date, y_position + 0.3, f"{event}", va='bottom', ha='center', fontsize=9, rotation=45)
    else:
        plt.text(date, y_position - 0.3, f"{event}", va='top', ha='center', fontsize=9, rotation=45)

# Remove y-ticks and y-labels
plt.yticks([])
plt.xlabel('Date')
plt.title('Timeline of Unsecured Debt')
plt.grid(True, axis='x')  # Only show grid on x-axis
plt.tight_layout()

# Show the plot
plt.show()
