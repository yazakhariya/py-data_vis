from pathlib import Path
import json

from typing import List

class EarthQuakesData:

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.magnitudes: List[float] = []
        self.longitudes: List[float] = []
        self.latitudes: List[float] = []

    def load_data(self) -> None: 
        try:
            contents = self.file_path.read_text()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at {self.file_path}")
        
        all_eq_data = json.loads(contents)
        all_eq_dicts = all_eq_data['features']

        for eq_dict in all_eq_dicts:
            self._process_data(eq_dict)

    def _process_data(self, eq_dict: List[str]) -> None:
        try:
            mag = eq_dict['properties']['mag']
            long = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]

            self.magnitudes.append(mag)
            self.longitudes.append(long)
            self.latitudes.append(lat)
        except (ValueError, IndexError) as e:
            print(f"Error {e}")

    # def visualize(self) -> None:
        
        
