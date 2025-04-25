from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('data_vis_csv/weather_data/death_valley_2021_simple.csv')

lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
dates, highs, lows = [], [], []

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])

    except ValueError:
        print(f"Missing date for {date}")

    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

title = "Daily temps , 2021\nDeath Valley, CA"
ax.set_title(title)
fig.autofmt_xdate()
ax.set_ylabel("Temperature Value (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()