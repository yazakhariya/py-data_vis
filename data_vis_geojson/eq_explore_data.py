from pathlib import Path
import json
import plotly.express as px
from typing import List

class EarthQuakesData:

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.magnitudes: List[float] = []
        self.longitudes: List[float] = []
        self.latitudes: List[float] = []
        self.eq_titles: List[str] = []
        self.map_title: str = ''

    def load_data(self) -> None: 
        try:
            contents = self.file_path.read_text(encoding="utf-8")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found at {self.file_path}") from e
        
        try:
            all_eq_data = json.loads(contents)
            all_eq_dicts = all_eq_data['features']
            self.map_title = all_eq_data['metadata']['title']

            for eq_dict in all_eq_dicts:
                self._process_data(eq_dict)
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError('Invalid GeoJSON data format') from e

    def _process_data(self, eq_dict: List[str]) -> None:
        try:
            self.magnitudes.append(eq_dict['properties']['mag'])
            self.longitudes.append(eq_dict['geometry']['coordinates'][0])
            self.latitudes.append(eq_dict['geometry']['coordinates'][1])
            self.eq_titles.append(eq_dict['properties']['title'])
        except (KeyError, IndexError) as e:
            print(f"Error {e}")

    def visualize(
            self,
            projection: str = 'natural earth',
            color_scale: str = 'Viridis',
        ) -> None:
        title = self.map_title
        fig = px.scatter_geo(lat=self.latitudes, lon=self.longitudes, title=title,
                color=self.magnitudes,
                color_continuous_scale=color_scale,
                labels={'color': 'Magnitude'},
                projection=projection,
                hover_name=self.eq_titles,
            )
        
        fig.show()
    

def main():
    try:
        data_file = Path('data_vis_geojson/eq_data/eq_1_day_m1.geojson')
        visualizer = EarthQuakesData(data_file)
        visualizer.load_data()
        visualizer.visualize(
            projection='natural earth',
            color_scale='Plasma'
        )
    except Exception as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    main()