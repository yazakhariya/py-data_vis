from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('data_vis_csv/weather_data/phoenix_2025.csv')

lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
dates, prcps, snows = [], [], []

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[3])
    except ValueError:
        print(f"Missing PRCP for {date}")
        continue 
    
    try:
        snow = float(row[4]) if len(row) > 4 else 0.0
    except ValueError:
        snow = 0.0  
    
    dates.append(date)
    prcps.append(prcp)
    snows.append(snow)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='orange', alpha=0.5)
ax.plot(dates, snows, color='blue', alpha=0.5)
ax.fill_between(dates, prcps, snows, facecolor='blue', alpha=0.1)

title = "Daily PRCP and Snow Data, January 2025\nPhoenix, AZ"
ax.set_title(title)
fig.autofmt_xdate()
ax.set_ylabel("PRCP (inches) & Snow", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()