# rokkashin
App that aggregates all earthquake data across Japan, generate map of hexes to see intensity, can layer different earthquakes/time periods together to raise/lower hexes like a 3d map

# Tasks
- Generalize and abstract logic to work generically
- Import more data
    - https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2023-01-01&endtime=2023-12-31&minmagnitude=3&minlatitude=24&maxlatitude=46&minlongitude=122&maxlongitude=146
- Add the ability to query data dynamically based on user input / eventually web UI
- Fine tune hex resolution and color until we find something that looks good
    - This will probably be a part of the frontend portion of this project and will be styled with CSS etc