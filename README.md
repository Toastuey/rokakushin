# rokkashin
App that aggregates all earthquake data across Japan, generate map of hexes to see intensity, can layer different earthquakes/time periods together to raise/lower hexes like a 3d map

# Tasks
- Add the ability to query data dynamically based on user input / eventually web UI
    - This will probably just be making different aggregates and plugging them into the visualize
- Fine tune hex resolution and color until we find something that looks good
    - This will probably be a part of the frontend portion of this project and will be styled with CSS etc
- Add function to draw fault lines
- Implement rest of data_io functions

# Checkpoint Goals
- Add the ability to playback earthquakes in sequence based on time
- Add the ability to click a hex and see details about all the earthquakes in that hex for the given date range
- Add the ability to change hex height based on other fields (Highest average magnitude, max magnitude, etc)
- Create interactive web app
