"""
This file is responsible for processing the created pandas dataframe to visualize data and generate a suitable HTML.
"""
from src import constants
import pydeck as pdk

def _fill_color(sortby=constants.FREQUENCY_MODE):
    """
    A function that defines the fill color for the hex map

    Args:
        param1: The sorting mode to base the color of hexes off of. | Defaults: constants.FREQUENCY_MODE
            
    Returns:
        A formatted string containing the range of color values to use for the hexes.
        
    Raises:
        None
    """
    match sortby:
        case constants.MIN_DEPTH_MODE | constants.MEAN_DEPTH_MODE:
            return f"[{constants.COLOR_R}, 0 + {constants.COLOR_VALUE}, {constants.COLOR_B}]"

        case constants.FREQUENCY_MODE | constants.MAX_MAGNITUDE_MODE | constants.MEAN_MAGNITUDE_MODE | constants.TOTAL_SEISMIC_MODE | _:
            return f"[{constants.COLOR_R}, 255 - {constants.COLOR_VALUE}, {constants.COLOR_B}]"


def render_map(agg, html_name, sorting_mode=constants.FREQUENCY_MODE):
    """
    Create a layer and HTML from the data.
    
    Args:
        param1: The aggregate data to build the map on.
        param2: Name of the output HTML.
        param3: The sorting mode to use for colors. | Defaults: constants.FREQUENCY_MODE
    Returns:
        None
        
    Raises:
        None
    """
    layer = pdk.Layer(
        "H3HexagonLayer",
        agg,
        get_hexagon=constants.HEX_ID,
        get_fill_color=_fill_color(sorting_mode),
        get_elevation=constants.HEIGHT_VALUE,
        elevation_scale=constants.ELEVATION_SCALE,
        extruded=True,
        pickable=True,
        opacity=constants.COLOR_OPACITY,
    )   

    view_state = pdk.ViewState(
        latitude=constants.INITIAL_LAT,
        longitude=constants.INITIAL_LON,
        zoom=4,
        pitch=80,
    )
    
    deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
    deck.to_html(html_name)
