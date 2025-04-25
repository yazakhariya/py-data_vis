from pathlib import Path
import json

path = Path('data_vis_geojson/eq_data/eq_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

path = Path('data_vis_geojson/eq_data/readable_eq_1_day_m1.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

