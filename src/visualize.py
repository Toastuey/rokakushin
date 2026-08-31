"""
This file is responsible for processing the created pandas dataframe to visualize data and generate a suitable HTML.
"""
from src import constants
import pydeck as pdk

def _fill_color():
    """
    A function that defines the fill color for the hex map

    Args:
        None
            
    Returns:
        None
        
    Raises:
        None
    """
    return f"[{constants.COLOR_R}, 255 - {constants.HEX_NAME} * {constants.COLOR_SENSITIVITY}, {constants.COLOR_B}]"


def render_map(agg, html_name):
    """
    Create a layer and HTML from the data.
    
    Args:
        param1: The aggregate data to build the map on.
        param2: Name of the output HTML.
        
    Returns:
        None
        
    Raises:
        None
    """
    layer = pdk.Layer(
        "H3HexagonLayer",
        agg,
        get_hexagon=constants.HEX_ID,
        get_fill_color=_fill_color(),
        get_elevation=constants.HEIGHT_VALUE,
        elevation_scale=constants.ELEVATION_SCALE,
        extruded=True,
        pickable=True,
        opacity=constants.COLOR_OPACITY,
    )   
    
    deck = pdk.Deck(layers=[layer])
    deck.to_html(html_name)
