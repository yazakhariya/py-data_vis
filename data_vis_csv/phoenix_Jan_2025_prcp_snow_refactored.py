from pathlib import Path
import csv
from datetime import datetime
from typing import List

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class WeatherDataVisualizer:

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.dates: List[datetime] = []
        self.precipitations: List[float] = []
        self.snowfalls: List[float] = []

    def load_data(self) -> None:
        try:
            lines = self.file_path.read_text().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Weather data file not found at {self.file_path}")
            
        reader = csv.reader(lines)
        next(reader)
        
        for row in reader:
            self._process_row(row)

    def _process_row(self, row: List[str]) -> None:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            prcp = float(row[3]) if row[3] else 0.0
            snow = float(row[4]) if len(row) > 4 and row[4] else 0.0

            self.dates.append(date)
            self.precipitations.append(prcp)
            self.snowfalls.append(snow)
        except (ValueError, IndexError) as error:
            print(f"Skipping row: {row}. Error {error}")

    def visualize(self) -> None:
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.autofmt_xdate(rotation=45, ha='right')
        ax.plot(self.dates, self.precipitations, color='orange', alpha=0.5, label="Precipitations")
        ax.plot(self.dates, self.snowfalls, color='blue', alpha=0.5, label="Snowfalls")
        ax.fill_between(self.dates, self.precipitations, self.snowfalls, facecolor='blue', alpha=0.1)

        self._configure_plot(ax)

        plt.legend()
        plt.tight_layout()
        plt.show()

    def _configure_plot(self, ax: plt.Axes) -> None:
        title = "Daily Precipitation and Snowfall - January 2025\nPhoenix, AZ"
        ax.set_ylabel("Amount (inches)", fontsize=12)
        ax.set_title(title, fontsize=14, pad=20)
        
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))


def main():
    try:
        data_file = Path('data_vis_csv/weather_data/phoenix_2025.csv')
        visualizer = WeatherDataVisualizer(data_file)
        visualizer.load_data()
        visualizer.visualize()
    except Exception as error:
        print(f"Error processing weather data: {error}")


if __name__ == '__main__':
    main()